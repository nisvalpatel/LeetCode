// Last updated: 10/9/2025, 8:10:42 PM
import java.util.HashMap;
class Solution {
    HashMap<Character, Integer> map = new HashMap<>();

 //helper function to change the dictionary for the magazine string
    public void changeMagazine(int i, String magazine){
        char z = magazine.charAt(i);
        int j = map.get(z);
        map.put(z, j+1);
    }

    private void changeNote(int i, String ransomNote){
        char z = ransomNote.charAt(i);
        int j = map.get(z);
        map.put(z, j-1);
    }

    public boolean canConstruct(String ransomNote, String magazine) {
        if (ransomNote.length() > magazine.length()){ return false;}

        //setting up the hashmap right now with the different characters
        for (char c = 'a'; c <= 'z'; c++){
            map.put(c, 0);
        }

        //with the dictionary set up, I am going to parse through the magazine since for this to work, it needs to be either the same size or larger than the ransomNote
        for (int i = 0; i < magazine.length(); i++){
            changeMagazine(i, magazine);
        }

        for (int i = 0; i < ransomNote.length(); i++){
            changeNote(i, ransomNote);
        }
        

        for (Integer value : map.values()) {
            if (value < 0){
                return false;
            }
        }
        return true;
    }
    
}