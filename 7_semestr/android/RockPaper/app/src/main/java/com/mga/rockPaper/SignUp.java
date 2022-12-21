package com.mga.rockpaper;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;

import com.mga.rockpaper.Db.DbHelper;

public class SignUp extends AppCompatActivity {

    EditText login, password, rePassword;
    Button makeReg;
    DbHelper dbHelper;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_sign_up);
        var actionBar=getSupportActionBar();
        actionBar.setTitle("Камень ножницы бумага");

        login = findViewById(R.id.loginSignUp);
        password = findViewById(R.id.passwordSignUp);
        rePassword = findViewById(R.id.rePasswordSignUp);

        makeReg = findViewById(R.id.makeRegisterButton);
        dbHelper=new DbHelper(this);
        makeReg.setOnClickListener(view -> {
            var loginText = login.getText().toString();
            var passwordText = password.getText().toString();
            var rePassText=rePassword.getText().toString();

            if(loginText.equals("") || passwordText.equals("") || rePassText.equals("")){
                Toast.makeText(SignUp.this,"Не все данные были введены!",Toast.LENGTH_SHORT).show();
                return;
            }
            var resOfCheckLogin=dbHelper.getLoginOperationProvider().checkLoginExists(loginText);
            if(resOfCheckLogin) {
                Toast.makeText(SignUp.this,"Логин уже имеется в системе!",Toast.LENGTH_SHORT).show();
                return;
            }

            if(!passwordText.equals(rePassText)){
                Toast.makeText(SignUp.this,"Пароли не совпадают!",Toast.LENGTH_SHORT).show();
                return;
            }

            var resOfAddLogin=dbHelper.getLoginOperationProvider().insertNewUser(loginText,passwordText);
            if(!resOfAddLogin)
            {
                Toast.makeText(SignUp.this,"Не удалось добавить пользователя(!",Toast.LENGTH_SHORT).show();
                return;
            }

            Toast.makeText(SignUp.this,"Пользователь добавлен!",Toast.LENGTH_LONG).show();
            Intent intent = new Intent(getApplicationContext(), MainActivity.class);
            startActivity(intent);
            this.finish();
        });
    }

    @Override
    public void onBackPressed() {
        this.finish();
    }
}