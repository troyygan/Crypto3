import javax.crypto.Cipher;
import javax.crypto.SecretKey;
import javax.crypto.SecretKeyFactory;
import javax.crypto.spec.DESKeySpec;
import java.security.SecureRandom;

public class DESTest {
    /*进行改变位数的辅助数组*/
    public static byte[][] b ;

    public static void main(String[] argv) {
        //初始化辅助数组
        initBytes();
        //初始明文
        String word = "AAAAAAAA";
        printTo8Binary("Initial Plaintext： " , word.getBytes());
        //初始秘钥
        String password = "12345678";
        printTo8Binary("Initial Key： " , password.getBytes());
        //加密
        byte[] result = desCrypto(word.getBytes(),password);
        printTo8Binary("Initial Ciphertext： " , result);

        /**改变明文位数**/
        for(int i = 1; i <= 64; i++) { //改变1-64位
            System.out.print("Clear Text Change "+i+"Bit： ");
            byte[] origin = word.getBytes(); //原始明文
            int digits = 0; //改变位数
            for(int j = 0; j < 10; j++) { //10种情况取平均
                byte[] now = new byte[8]; //现在明文
                for(int k = 0; k < origin.length; k++) { //用辅助数组进行变位（i-1位）
                    now[k] = (byte)(origin[k] ^ b[i-1][k]);
                }
                bytesMoveToRight(1 , b[i-1]); //右移一下辅助数组，供下种情况使用
//                printTo8Binary("Change"+(j+1)+"After Plaintext： " , now);
                //加密
                byte[] r = desCrypto(now,password);
//                printTo8Binary("Change"+(j+1)+"Post Ciphertext： " , r);
                digits += countBitDiff(r , result);//和原始密文比较，记录改变位数
//                System.out.println("密文改变了"+countBitDiff(r , result)+"位");
            }
            System.out.println("Mean Cipher Change"+(double)digits/10.0+" Bit");
        }

        /**改变秘钥位数**/
        for(int i = 1; i <= 64; i++) { //改变1-64位
            System.out.print("Key Change "+i+" Bit： ");
            byte[] origin = password.getBytes();//原始秘钥
            int digits = 0; //改变位数
            for(int j = 0; j < 10; j++) { //10种情况取平均
                byte[] now = new byte[8]; //现在秘钥
                for(int k = 0; k < origin.length; k++) { //用辅助数组进行变位（i-1位）
                    now[k] = (byte)(origin[k] ^ b[i-1][k]);
                }
                bytesMoveToRight(1 , b[i-1]); //右移一下辅助数组，供下种情况使用
//                printTo8Binary("Changed key： " , now);
                //加密
                byte[] r = desCrypto(now,password);
//                printTo8Binary("Changed Ciphertext： " , r);
                digits += countBitDiff(r , result);//和原始密文比较，记录改变位数
            }
            System.out.println("The Ciphertext Changed on Average "+(double)digits/10.0+" Bit");
        }

    }

    /**
     * 加密方法
     * @param datasource 明文
     * @param password 秘钥
     * @return 密文
     */
    public static byte[] desCrypto(byte[] datasource, String password) {
        try{
            SecureRandom random = new SecureRandom();
            DESKeySpec desKey = new DESKeySpec(password.getBytes());
            //创建一个密匙工厂，然后用它把DESKeySpec转换成
            SecretKeyFactory keyFactory = SecretKeyFactory.getInstance("DES");
            SecretKey securekey = keyFactory.generateSecret(desKey);
            //Cipher对象实际完成加密操作
            Cipher cipher = Cipher.getInstance("DES/ECB/NoPadding");
            //用密匙初始化Cipher对象
            cipher.init(Cipher.ENCRYPT_MODE, securekey, random);
            //现在，获取数据并加密
            //正式执行加密操作
            return cipher.doFinal(datasource);
        }catch(Throwable e){
            e.printStackTrace();
        }
        return null;
    }

    /**
     * 把byte类型转换为8位二进制类型字符串输出
     * @param tByte
     * @return
     */
    public static void printTo8Binary(String pre, byte[] tByte) {
        System.out.print(pre);
        for(int i=0; i<tByte.length; i++) {
            String tString = Integer.toBinaryString((tByte[i] & 0xFF) + 0x100).substring(1);
            System.out.print(tString + " ");
        }
        System.out.println();
    }

    /**
     * 初始化辅助数组
     */
    public static void initBytes() {
        b = new byte[64][8];
        b[0][0] = -128;
        for(int i = 1; i < 64; i++) {
            for(int j = 0; j < 8; j++) {
                b[i][j] = b[i-1][j];
            }
            int k = i/8;
            int z = (i+1)%8; z = z == 0 ? 8 : z;
            b[i][k] ^= (byte) Math.pow(2, (8-z));
        }
    }

    /**
     * 循环右移一个byte数组
     * @param num 右移位数
     * @param b 数组
     * @return 右移后数组
     */
    public static byte[] bytesMoveToRight(int num , byte[] b) {
        byte[] bytes = b;
        for(int i = 0; i < num; i++) {
            byte low = (byte)(bytes[bytes.length-1] & 1);
            for(int j = 0; j < bytes.length; j++) {
                byte loww = (byte)(bytes[j] & 1);
                bytes[j] = (byte)(bytes[j]>>1&127);
                bytes[j] = (byte) (bytes[j] ^ (low<<7) );
                low = loww;
            }
        }
        return bytes;
    }

    /**
     * 求两个字节数组的二进制中不同的位数
     * @param m
     * @param n
     * @return 返回不同的位数的个数
     */
    public static int countBitDiff(byte[] m, byte[] n) {
        if(m.length != n.length) return -1;

        byte[] ans = new byte[m.length];
        for(int i = 0; i < m.length; i++) {
            ans[i] =(byte) (m[i] ^ n[i]);
        }
        int count = 0;
        for(int i = 0; i < ans.length; i++) {
            while(ans[i] != 0){
                ans[i] &= (byte)(ans[i] -1);
                count++;
            }
        }
        return count;
    }
}
