package com.example.legacy;

// A simple Plain Old Java Object (POJO) to represent a user.
// In a real legacy app, this might have more complex logic.
public class LegacyUser {

    private String userName;
    private String userEmail;
    private int userId;

    public LegacyUser(int id, String name, String email) {
        this.userId = id;
        this.userName = name;
        this.userEmail = email;
    }

    public String getUserName() {
        return userName;
    }

    public void setUserName(String userName) {
        this.userName = userName;
    }

    public String getUserEmail() {
        return userEmail;
    }

    public int getUserId() {
        return userId;
    }

    public void displayUserInfo() {
        System.out.println("User ID: " + this.userId);
        System.out.println("User Name: " + this.userName);
    }
}