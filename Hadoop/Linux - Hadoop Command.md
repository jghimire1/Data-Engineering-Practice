# Linux Command 
        1  cd 
        2  ls 
        3  cd startApps
        4  ls 
        5  pwd 
        6  sh restartHadoop.sh 
        7  jps 
        8  ls 
        9  sh stopHadoop.sh 
        10  cd 
        11  cd
        12  exit
        13  cd 
        14  ls 
        15  
        16  pw 
        17  pwd 
        18  mkdir data
        19  ls 
        20  cd data 
        21  ls
        22  mkdir data1/data2 
        23  
        24  
        25  mkdir -p data1/data2
        26  ls
        27  cd data1/
        28  ls 
        29  pwd 
        30  cd data2
        31  cd 
        32  pwd 
        33  cd data/data1/data2
        34  cd ..
        35  cd ../..
        36  
        37  cd .
        38  ls 
        39  rm -r data
        40  ls 
        41  ls / 
        42  ls data1/
        43  ls data1/data2
        44  touch emp.txt
           45  ls 
           46  ls -l
           47  nano emp.txt
           48  ls -l 
           49  nano emp.txt
           50  ls -l
           51  cp emp.txt data1/
           52  ls 
           53  ls data1/
           54  cd data1
           55  ls 
           56  mv emp.txt data2/
           57  ls 
           58  ls data2/
           59  cat emp.txt 
           60  cat data2/emp.txt
           61  history 
           62  cd 
           63  la
           64  ls
           65  cd sartApps/
           66  cd startApps/
           67  sh restartHadoop.sh
           68  jps
           69  clear 
           70  ls 
           71  
           72  hadoop fs -ls 
           73  hadoop fs -mkdir -p user/test
           74  hadoop fs - ls /user
           75  hadoop fs -ls
           76  cd 
           77  hadoop fs -ls /user
           78  cd 
           79  cd data 
           80  nano zipcodes.csv
           81  LS 
           82  ls
           83  hadoop fs -mkdir -p /user/test/data
           84  ls
           85  hadoop fs -ls /user/test/data
           86  hadoop fs -put zipcodes.csv /user/test/data
           87  hadoop fs -ls /user/test/data
           88  cd data1
           89  ls 
           90  history 
           91  clear
           92  ls 
           93  hadoop fs -get /user/test/data/zipcodes.csv .
           94  ls 
           95  cat zipcodes.csv
           96  clear 
           97  hadoop fs -cat user/test/data/zipcodes.csv
           98  rm zipcodes.csv
           99  ls 
          100  rm data2
          101  ls 
          102  hadoop fs -rm /user/test/data/zipcodes.csv
          103  hadoop fs -ls /user/test/data
          104  hadoop fs -rm -r /user/test/data
          105  ls 
          106  cd ..
          107  ls 
          108  cat zipcodes.csv | head -n 2
          109  cat zipcodes.csv | tail -n 2
          110  hadoop fs -mkdir -p /user/test/data 
          111  hadoop fs -put zipcodes.csv /user/test/data
          112  hadoop fs -cat /user/test/data/zipcodes.csv | head -n 2
          113  hadoop fs -cat /user/test/data/zipcodes.csv | tail -n 2
          114  hadoop fs -du /user/test/data/zipcodes.csv
          115  hadoop fs -mkdir /user/test/data1
          116  hadoop fs -ls /user/test
          117  hadoop fs -mv /user/test/data/zipcodes.csv /user/test/data1/
          118  hadoop fs -ls /user/test/data
          119  hadoop fs -ls /user/test/data1
          120  ls 
          121  cp zipcodes.csv zipcodes1.csv
          122  ls 
          123  hadoop fs -mkdir -p /user/test/data2
          124  hadoop fs -moveFromLocal zipcodes1.csv /user/test/data2/
          125  ls
          126  hadoop fs -ls user/test/data2
          127  hadoop fs -ls /user/test/data2
          128  history

   
        
