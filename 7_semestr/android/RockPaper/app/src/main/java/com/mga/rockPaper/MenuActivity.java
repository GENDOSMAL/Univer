package com.mga.rockpaper;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.widget.Button;
import android.widget.TextView;
import android.widget.Toast;

public class MenuActivity extends AppCompatActivity {

    String login;

    TextView loginInfoTextView;
    Button startGameButton, statButton, changeAccountButton, exitButton;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_menu);

        var actionBar = getSupportActionBar();
        actionBar.setTitle("Камень ножницы бумага");

        var intent = getIntent();
        login = intent.getStringExtra("login");

        loginInfoTextView=findViewById(R.id.loginInfo);
        loginInfoTextView.setText("Добро пожаловать, "+login);

        startGameButton = findViewById(R.id.startGameButton);
        statButton = findViewById(R.id.statButton);
        changeAccountButton = findViewById(R.id.changeAccountButton);
        exitButton = findViewById(R.id.exitButton);

        exitButton.setOnClickListener(view -> {
            this.finish();
            System.exit(0);
        });

        changeAccountButton.setOnClickListener(view -> {
            Intent loginIntent = new Intent(getApplicationContext(), MainActivity.class);
            startActivity(loginIntent);
            this.finish();
        });

        startGameButton.setOnClickListener(view -> {
            Intent gameActivity = new Intent(getApplicationContext(), GameActivity.class);
            gameActivity.putExtra("login", login);
            startActivity(gameActivity);
        });

        statButton.setOnClickListener(view -> {
            Intent statActivity = new Intent(getApplicationContext(), StatActivity.class);
            statActivity.putExtra("login", login);
            startActivity(statActivity);
        });
    }

    @Override
    public void onBackPressed() {
        this.finish();
    }
}