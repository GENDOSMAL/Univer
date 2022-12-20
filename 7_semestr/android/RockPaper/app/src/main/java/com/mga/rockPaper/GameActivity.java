package com.mga.rockpaper;

import static android.content.ContentValues.TAG;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;
import android.widget.Toast;

import com.mga.rockpaper.Db.DbHelper;
import com.mga.rockpaper.Models.StatInfo;

import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;
import java.util.concurrent.ThreadLocalRandom;

public class GameActivity extends AppCompatActivity {
    TextView userChoiceTextView, compChoiceTextView, scoreTextView, wonInfoTextView;
    Button returnButton;

    String login;
    int userScore, compScore;

    DbHelper dbHelper;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_game);
        var actionBar = getSupportActionBar();
        actionBar.setTitle("Камень ножницы бумага");

        var intent = getIntent();
        login = intent.getStringExtra("login");
        userScore = 0;
        compScore = 0;

        returnButton = findViewById(R.id.returnButton);

        userChoiceTextView = findViewById(R.id.userSelectedTextView);
        compChoiceTextView = findViewById(R.id.compSelectedTextView);
        scoreTextView = findViewById(R.id.scoreTextView);
        wonInfoTextView = findViewById(R.id.wonInfoTextView);
//        setScoreTextView();
        userChoiceTextView.setText("");
        compChoiceTextView.setText("");
        wonInfoTextView.setText("");
        dbHelper=new DbHelper(this);
        returnButton.setOnClickListener(view -> {
            saveStat();
            this.finish();
        });
    }

    @Override
    public void onBackPressed() {
        saveStat();
        this.finish();
    }

    public void rpsButtonSelected(View view) {
        var userSelection = Integer.parseInt(view.getTag().toString());
        userChoiceTextView.setText(getTextById(userSelection));
        var compChoiceId = getRandomInt();
        Log.i(TAG, "Комп выбрал: " + compChoiceId);
        Log.i(TAG, "Юзер выбрал: " + userSelection);
        compChoiceTextView.setText(getTextById(compChoiceId));

        if (userSelection == compChoiceId) {
            wonInfoTextView.setText("Ничья");
        }

        if(userSelection==1) {
            if(compChoiceId==2){
                userWin();
            }
            else if(compChoiceId==3){
                compWin();
            }
        }else if (userSelection==2){
            if(compChoiceId==1){
                compWin();
            }else if (compChoiceId==3){
                userWin();
            }
        }else if (userSelection==3){
            if(compChoiceId==1){
                userWin();
            }else if (compChoiceId==2){
                compWin();
            }
        }
    }

    private void saveStat(){
        if(userScore==0 && compScore==0)
            return;

        DateTimeFormatter dtf = DateTimeFormatter.ofPattern("dd.MM.yyyy HH:mm:ss");
        LocalDateTime now = LocalDateTime.now();
        var statInfo=new StatInfo();
        statInfo.login=login;
        statInfo.timeOfPlay=dtf.format(now);
        statInfo.userScore=userScore;
        statInfo.compScore=compScore;
        var saveResult=dbHelper.getStatOperationProvider().insertData(statInfo);
        if(saveResult){
            Toast.makeText(GameActivity.this,"Данные сохранены в статистику успешно!",Toast.LENGTH_SHORT).show();
        }else{
            Toast.makeText(GameActivity.this,"Не удалось сохранить данные в статистику!",Toast.LENGTH_SHORT).show();
        }
    }

    private void setScoreTextView() {
        var scoreString = userScore + " : " + compScore;
        scoreTextView.setText(scoreString);
    }

    private String getTextById(int id) {
        if (id == 1)
            return "КАМЕНЬ";
        else if (id == 2)
            return "НОЖНИЦЫ";
        else
            return "БУМАГА";
    }

    private int getRandomInt() {
        return ThreadLocalRandom.current().nextInt(1, 4);
    }

    private void compWin(){
        compScore=compScore+1;
        wonInfoTextView.setText("Компьютер победил(");
        setScoreTextView();
    }

    private void userWin(){
        userScore=userScore+1;
        wonInfoTextView.setText("Ура победа!");
        setScoreTextView();
    }
}