package com.cheezestudio.diceapplication;

import android.media.MediaPlayer;
import android.os.Bundle;
import android.widget.Button;
import android.widget.ImageView;

import androidx.appcompat.app.AppCompatActivity;

import com.daimajia.androidanimations.library.Techniques;
import com.daimajia.androidanimations.library.YoYo;

import java.util.Random;

public class MainActivity extends AppCompatActivity {

    private MediaPlayer mediaPlayer;
    private ImageView dice;
    private Button rollDice;
    private boolean isRolling = false;

    private int[] diceIds = {R.drawable.dice_1, R.drawable.dice_2, R.drawable.dice_3, R.drawable.dice_4, R.drawable.dice_5, R.drawable.dice_6};

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        mediaPlayer = MediaPlayer.create(this, R.raw.roll_dice);
        dice = findViewById(R.id.dice);
        rollDice = findViewById(R.id.roll_dice);

        rollDice.setOnClickListener(view -> {
            if (!isRolling) {
                isRolling = true;

                if (mediaPlayer != null) {
                    mediaPlayer.start();
                }

                YoYo.with(Techniques.Shake).duration(700).onEnd(animator -> {
                    Random random = new Random();
                    int randomIndex = random.nextInt(diceIds.length);
                    int randomDiceId = diceIds[randomIndex];
                    dice.setImageResource(randomDiceId);

                    isRolling = false;
                }).playOn(dice);
            }
        });
    }

    @Override
    protected void onDestroy() {
        super.onDestroy();
        if (mediaPlayer != null) {
            mediaPlayer.release();
            mediaPlayer = null;
        }
    }
}