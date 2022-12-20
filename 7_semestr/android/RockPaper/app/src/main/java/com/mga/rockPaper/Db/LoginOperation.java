package com.mga.rockpaper.Db;

import android.content.ContentValues;
import android.database.Cursor;
import android.database.sqlite.SQLiteDatabase;

public class LoginOperation {
    private SQLiteDatabase _dbProvider;

    LoginOperation (SQLiteDatabase dbProvider){
        _dbProvider=dbProvider;
    }

    public Boolean insertNewUser(String login, String password) {
        ContentValues contentValues = new ContentValues();
        contentValues.put("login", login);
        contentValues.put("password", password);
        var result = _dbProvider.insert("users", null, contentValues);
        return result != -1;
    }

    public Boolean checkLoginExists(String login) {
        Cursor cursor = _dbProvider.rawQuery("Select * from users where login=?", new String[]{login});
        var res = cursor.getCount() > 0;
        cursor.close();
        return res;
    }

    public Boolean checkLoginAndPassword(String login, String password) {
        Cursor cursor = _dbProvider.rawQuery("Select * from users where login=? and password=?", new String[]{login, password});
        var res = cursor.getCount() > 0;
        cursor.close();
        return res;
    }

}
