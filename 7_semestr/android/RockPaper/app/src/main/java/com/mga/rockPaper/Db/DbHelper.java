package com.mga.rockpaper.Db;

import android.content.Context;
import android.database.sqlite.SQLiteDatabase;
import android.database.sqlite.SQLiteOpenHelper;

import androidx.annotation.Nullable;

public class DbHelper extends SQLiteOpenHelper {
    public static final String DBName = "RockPaperDB.sqlite";

    public DbHelper(@Nullable Context context) {
        super(context, DBName, null, 1);
    }

    @Override
    public void onCreate(SQLiteDatabase sqLiteDatabase) {
        sqLiteDatabase.execSQL("create Table users(login TEXT primary key, password TEXT)");
        sqLiteDatabase.execSQL("create Table userScore(id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,login TEXT,dateAndTimeOfPlay Text," +
                "userScore INTEGER, compScore INTEGER)");
    }

    @Override
    public void onUpgrade(SQLiteDatabase sqLiteDatabase, int i, int i1) {
        clearDb(sqLiteDatabase);
    }

    public LoginOperation getLoginOperationProvider() {
        return new LoginOperation(this.getWritableDatabase());
    }

    public StatOperation getStatOperationProvider() {
        return new StatOperation(this.getWritableDatabase());
    }

    private void clearDb(SQLiteDatabase db) {
        db.execSQL("drop Table if exists users");
    }
}
