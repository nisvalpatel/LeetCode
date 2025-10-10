// Last updated: 10/9/2025, 8:10:51 PM
class Solution {

    public String addBinary(String a, String b) {
        StringBuilder sb = new StringBuilder();
        int carry = 0;
        int i = a.length() - 1;
        int j = b.length() - 1;
        int temp;
        int A;
        int B;


        while (i >= 0 || j >= 0 || carry == 1){
            if (i < 0 && j < 0 ){
                sb.append(carry);
                carry = 0;

            } else if (i < 0){
                temp = (b.charAt(j) - '0') + carry;
                sb.append(temp%2);
                carry = temp / 2;

            }else if (j < 0){
                temp = (a.charAt(i) - '0') + carry;
                sb.append(temp%2);
                carry = temp / 2;

            }else{
                A = a.charAt(i) - '0';
                B = b.charAt(j) - '0';
                temp = A + B + carry;
                sb.append(temp%2);
                carry = temp / 2;
            }
            i -= 1;
            j -= 1;
        }
        return sb.reverse().toString();

    }
}