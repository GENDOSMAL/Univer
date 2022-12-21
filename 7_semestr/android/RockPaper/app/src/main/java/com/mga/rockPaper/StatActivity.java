package com.mga.rockpaper;

import static android.content.ContentValues.TAG;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.util.Log;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TableLayout;
import android.widget.TableRow;
import android.widget.TextView;
import android.widget.Toast;

import com.mga.rockpaper.Db.DbHelper;

public class StatActivity extends AppCompatActivity {

    TextView infoForUser;
    String login;
    TableLayout tableLayout;
    Button returnButton;

    DbHelper dbHelper;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_stat);
        var actionBar = getSupportActionBar();
        actionBar.setTitle("Камень ножницы бумага");

        var intent = getIntent();
        login = intent.getStringExtra("login");

        infoForUser = findViewById(R.id.informatinText);
        tableLayout = findViewById(R.id.statTable);
        returnButton = findViewById(R.id.returnButtonStat);
        dbHelper = new DbHelper(this);
        infoForUser.setText("Стата игр пользователя: " + login);
        fillTable();
        returnButton.setOnClickListener(view -> {
            finalD();
        });
    }

    @Override
    public void onBackPressed() {
        this.finish();
    }

    private void finalD() {
        this.finish();
    }

    private void fillTable() {
        try {


            var loadedData = dbHelper.getStatOperationProvider().selectUserStatInfo(login);
            if (loadedData.stream().count() == 0) {
                Toast.makeText(StatActivity.this, "Не найдено статы для пользователя!", Toast.LENGTH_LONG).show();
                return;
            }

            for (var data : loadedData) {
                TableRow row = new TableRow(this);
                var idTextView = new TextView(this);
                idTextView.setText(String.valueOf(data.id));
                row.addView(idTextView);

                var timeTextView = new TextView(this);
                timeTextView.setText(data.timeOfPlay);
                row.addView(timeTextView);

                var userWin = new TextView(this);
                userWin.setText(String.valueOf(data.userScore));
                row.addView(userWin);

                var compWin = new TextView(this);
                compWin.setText(String.valueOf(data.compScore));
                row.addView(compWin);
                tableLayout.addView(row);
            }
        } catch (Exception ex) {
            Log.e(TAG, "Ошибка(", ex);
        }
    }
}