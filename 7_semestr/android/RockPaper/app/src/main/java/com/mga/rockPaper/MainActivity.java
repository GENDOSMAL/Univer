package com.mga.rockpaper;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;

import com.mga.rockpaper.Db.DbHelper;

public class MainActivity extends AppCompatActivity {

    EditText login,password;
    Button signUp,sign;

    DbHelper dbHelper;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        var actionBar=getSupportActionBar();
        actionBar.setTitle("Камень ножницы бумага");

        login= findViewById(R.id.login);
        password= findViewById(R.id.password);

        sign= findViewById(R.id.signButton);
        signUp= findViewById(R.id.signUpButton);

        dbHelper=new DbHelper(this);

        sign.setOnClickListener(view -> {
            String loginText=login.getText().toString();
            String passwordText=password.getText().toString();
            Boolean checkUserExistResult=dbHelper.getLoginOperationProvider().checkLoginAndPassword(loginText,passwordText);
            if(checkUserExistResult){
                Intent intent = new Intent(getApplicationContext(), MenuActivity.class);
                intent.putExtra("login",loginText);
                startActivity(intent);
                finish();
                return;
            }
            Toast.makeText(MainActivity.this,"Логин или пароль не правильный!",Toast.LENGTH_SHORT).show();
        });

        signUp.setOnClickListener(view -> {
            Intent intent = new Intent(getApplicationContext(), SignUp.class);
            startActivity(intent);
        });
    }

    @Override
    public void onBackPressed() {
        this.finish();
    }
}