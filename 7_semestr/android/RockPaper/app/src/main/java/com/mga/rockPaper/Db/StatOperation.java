package com.mga.rockpaper.Db;

import static android.content.ContentValues.TAG;
import static android.webkit.ConsoleMessage.MessageLevel.LOG;

import android.content.ContentValues;
import android.database.Cursor;
import android.database.sqlite.SQLiteDatabase;
import android.util.Log;

import com.mga.rockpaper.Models.StatInfo;

import java.util.ArrayList;
import java.util.List;

public class StatOperation {
    private SQLiteDatabase _dbProvider;
    StatOperation (SQLiteDatabase dbProvider){
        _dbProvider=dbProvider;
    }

    public boolean insertData(StatInfo info){
        ContentValues contentValues = new ContentValues();
        contentValues.put("login", info.login);
        contentValues.put("dateAndTimeOfPlay", info.timeOfPlay);
        contentValues.put("compScore", info.compScore);
        contentValues.put("userScore", info.userScore);

        var result = _dbProvider.insert("userScore", null, contentValues);
        return result != -1;
    }

    public List<StatInfo> selectUserStatInfo(String userLogin){
        var res=new ArrayList<StatInfo>();
        var cursor = _dbProvider.rawQuery("Select * from userScore where login=?", new String[]{userLogin});
        if(cursor.moveToFirst()){
            while (!cursor.isAfterLast()) {
                var obj=new StatInfo();
                var indOfId=cursor.getColumnIndex("id");
                if(indOfId!=-1){
                    obj.id = Integer.parseInt(cursor.getString(indOfId));
                }
                var indOfDateAndTimeOfPlay=cursor.getColumnIndex("dateAndTimeOfPlay");
                if(indOfDateAndTimeOfPlay!=-1){
                    obj.timeOfPlay = cursor.getString(indOfDateAndTimeOfPlay);
                }
                var indOfcompScore=cursor.getColumnIndex("compScore");
                if(indOfcompScore!=-1){
                    obj.compScore = Integer.parseInt(cursor.getString(indOfcompScore));
                }

                var indOfuserScore=cursor.getColumnIndex("userScore");
                if(indOfuserScore!=-1){
                    obj.userScore = Integer.parseInt(cursor.getString(indOfuserScore));
                }
                obj.login=userLogin;
                res.add(obj);
                cursor.moveToNext();
            }
        }
        Log.i(TAG,"Найдено данных по логину "+userLogin+" "+res.stream().count());
        return res;
    }
}
