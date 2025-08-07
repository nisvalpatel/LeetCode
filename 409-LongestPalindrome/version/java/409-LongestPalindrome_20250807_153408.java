// Last updated: 8/7/2025, 3:34:08 PM

class Solution {
    public int longestPalindrome(String s) {
        //Declaring the List since we won't be incrementing the list size
        int[] tempList = new int[52];

        //Declaring the variables I may need for the 
        char tempChar;
        
        for (int i = 0; i < s.length(); i++){
            tempChar = s.charAt(i);    //Find what char is on this index of the string

            if (tempChar > 96){   //The number 97 is the start of the ascii for 'a'
                tempChar -= 97; //setting the char relative to the alphabet and list
                tempList[tempChar] += 1;


            }else{ //Getting the upper case Characters
                tempChar -= 65 - 26;
                tempList[tempChar] += 1;
            }
        }
        int sum = 0;

        for (int i = 0; i < 52; i++){
            sum = sum + (tempList[i]/2);
        }
        if (sum * 2 < s.length()){
            return (sum*2) + 1;
        }else{
            return sum * 2;
        }
    
        

    }
    
}