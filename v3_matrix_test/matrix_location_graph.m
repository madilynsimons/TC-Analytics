
fid = fopen('out.csv');
out = textscan(fid, '%f%f', 'delimiter', ',');
fclose(fid);

x = out{1};
y = out{2};

plot(x, y);