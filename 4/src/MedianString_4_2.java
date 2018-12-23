import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;

public class MedianString_4_2 {

    private static Integer k;
    private static ArrayList<String> dna;

    private static String amins = "ACGT";

    public static void permute(int length, String prefix, ArrayList<String> list ) {
        if(length == 0) {
            list.add(prefix);
            return;
        }
        for(int i = 0; i < amins.length(); ++i) {
            permute(length - 1,prefix + amins.charAt(i),list);
        }
    }

    public static int hammingDistance( String p, String q ) {
        if(p.length() != q.length()) {
            System.out.println("P and Q are different lengths!");
            System.exit(-1);
        }
        int mismatch = 0;
        for(int i = 0; i < p.length(); ++i) {
            if(p.charAt(i) != q.charAt(i))
                ++mismatch;
        }
        return mismatch;
    }

    private static void readData(){
        try{
            BufferedReader bufferRead = new BufferedReader(new InputStreamReader(System.in));

            k = Integer.parseInt(bufferRead.readLine());

            for(int i = 0; i < 2 * k; i++){
                dna.add(bufferRead.readLine());
            }

            //System.out.println(dna);

        }
        catch(Exception ex)
        {
            ex.printStackTrace();
        }
    }

    private static Integer distanse(String pattern, String dna_i){

        Integer minDistanse = Integer.MAX_VALUE;
        for(int i = 0; i < dna_i.length() - k + 1; i++){
            String kMer = dna_i.substring(i, i + k);
            Integer distanse = hammingDistance(pattern, kMer);
            if(distanse < minDistanse){
                minDistanse = distanse;
            }
        }

        return minDistanse;
    }

    private static Integer distanse(String pattern, ArrayList<String> dna){

        Integer distanse =  0;

        for(String dna_i : dna){
            distanse += distanse(pattern, dna_i);
        }

        return distanse;
    }

    private  static String medianString(){

        String median = "";
        Integer distanse = Integer.MAX_VALUE;
        ArrayList<String> kMerPatterns = new ArrayList<>();
        permute(k, "", kMerPatterns);

        for(String kMerPattern : kMerPatterns){
            //System.out.println(kMerPattern);
            Integer tmpDistanse = distanse(kMerPattern, dna);
            if(distanse > tmpDistanse){
                distanse = tmpDistanse;
                median = kMerPattern;
            }
        }


        return median;
    }

    public static void main(String[] args) {
        dna = new ArrayList<>();
        //System.out.println("Data: ");
        readData();
        System.out.println(medianString());
    }

}
