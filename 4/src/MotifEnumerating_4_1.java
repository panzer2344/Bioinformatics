import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;

public class MotifEnumerating_4_1 {

    private static Integer k;
    private static Integer d;
    private static ArrayList<String> dna;

    private static String amins = "ACGT";


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

    public static void permute(int length, String prefix, ArrayList<String> list ) {
        if(length == 0) {
            list.add(prefix);
            return;
        }
        for(int i = 0; i < amins.length(); ++i) {
            permute(length - 1,prefix + amins.charAt(i),list);
        }
    }

    private static List<String> differingPatterns(String pattern, Integer d){


        ArrayList<String> output = new ArrayList<>();
        permute(pattern.length(),"", output);
        for(int i = 0; i < output.size(); ++i) {
            if(hammingDistance(pattern,output.get(i)) > d) {
                output.remove(i--);
            }
        }

        return output;

    }

    private static List<String> kMerPatterns(List<String> dna, Integer k, Integer row){

        ArrayList<String> patterns = new ArrayList<>();
        String firstRow = dna.get(row);
        for(int i = 0; i < firstRow.length() - k + 1; i++){
            patterns.add(firstRow.substring(i, i + k));
        }

        return patterns;

    }

    private static Boolean appearsInEachString(List<String> dna, String pattern, Integer k, Integer d){
        Integer count = 0;

        for(int i = 1; i < dna.size(); i++) {
            String row = dna.get(i);
            Boolean isInRow = false;
            for(int j = 0; j < row.length() - k + 1; j++){
                if(hammingDistance(row.substring(j, j + k), pattern) <= d){
                    isInRow = true;
                }
            }
            if(isInRow){
                count++;
            }
        }

        return count.equals(dna.size() - 1);
    }

    private static HashSet<String> motifEnumeration(List<String> dna, Integer k, Integer d){

        HashSet<String> patterns = new HashSet<>();

        for(String pattern : kMerPatterns(dna, k, 0)){
            for(String pattern_ : differingPatterns(pattern, d)){
                if(appearsInEachString(dna, pattern_, k, d)){
                    //System.out.println(pattern_);
                    patterns.add(pattern_);
                }
            }
        }

        return patterns;
    }

    private static void readData(){
        try{
            BufferedReader bufferRead = new BufferedReader(new InputStreamReader(System.in));

            String integers = bufferRead.readLine();
            k = Integer.parseInt(integers.split(" ")[0]);
            d = Integer.parseInt(integers.split(" ")[1]);

            for(int i = 0; i < k; i++){
                dna.add(bufferRead.readLine());
            }

            //System.out.println(dna);

        }
        catch(Exception ex)
        {
            ex.printStackTrace();
        }
    }

    private static void printMotifs(List<String> motifs){
        for(String motif : motifs){
            System.out.print(motif + " ");
        }
    }

    public static void main(String[] args) {

        dna = new ArrayList<>();
        //System.out.println("Data: ");
        readData();
        HashSet<String> motifs = motifEnumeration(dna, k, d);
        ArrayList<String> sortedUniqueMotifs = new ArrayList<>(motifs);
        Collections.sort(sortedUniqueMotifs);
        //System.out.println(sortedUniqueMotifs);
        printMotifs(sortedUniqueMotifs);

    }

}
