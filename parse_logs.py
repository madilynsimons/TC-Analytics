import os

def to_milliseconds(time):
    arr = time[1:12].split("_")
    hours = int(arr[0]) * 3600000
    minutes = int(arr[1]) * 60000
    seconds = int(arr[2]) * 1000
    milliseconds = int(arr[3])
    return milliseconds + seconds + minutes + hours

def printTime(time_start, time_end, out_file):
   total_time = time_end - time_start
   out_file.write("%d\n" % total_time)

def printError(write_file):
   write_file.write("Picture error")

def parseFile(read_name, write_name):
   read_file = open(read_name, "r")
   write_file = open(write_name, "w")
   time_start = -1
   time_end = -1
   for reading in read_file:
      line = reading.split()
      if line[1] == "TAKE" and line[2] == "PICTURE":
         if line[3] == "BEGIN":
            time_start = to_milliseconds(line[0])
         elif line[3] == "END":
            if time_start != -1 and time_end == -1:
               time_end = to_milliseconds(line[0])
               printTime(time_start, time_end, write_file)
               time_start = -1
               time_end = -1
            else:
               printError(write_file)

def printFinalData(file_name1, file_name2):
   file1 = open(file_name1, "r")
   file2 = open(file_name2, "r")

   file1_data = []
   file2_data = []

   for data in file1:
      file1_data.append(int(data))

   for data in file2:
      file2_data.append(int(data))

   final_results = open("final_data.txt", "w")
   final_results.write("FOTOAPPARAT\n")
   final_results.write("Average time: %d\n" % float(sum(file1_data)/len(file1_data)))
   final_results.write("Max time: %d\n" % max(file1_data))
   final_results.write("Min time: %d\n" % min(file1_data))
   final_results.write("\n")

   final_results.write("GOOGLE CAMERA\n")
   final_results.write("Average time: %d\n" % float(sum(file2_data)/len(file2_data)))
   final_results.write("Max time: %d\n" % max(file2_data))
   final_results.write("Min time: %d\n" % min(file2_data))
   final_results.write("\n")

def main():
   fotoapparat_file_name_in = "fotoapparat_100pictures.txt"
   fotoapparat_file_name_out = "fotoapparat_out.txt"
   parseFile(fotoapparat_file_name_in, fotoapparat_file_name_out)

   googlecam_file_name_in = "camera_100pictures.txt"
   googlecam_file_name_out = "camera_out.txt"
   parseFile(googlecam_file_name_in, googlecam_file_name_out)

   printFinalData(fotoapparat_file_name_out, googlecam_file_name_out)

main()
