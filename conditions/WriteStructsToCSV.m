function WriteStructsToCSV(filename, theStructs)
% WriteStructsToText(filename,theStructs)
%
% Write a tab delimited text file.  The first row should
% contain the field names for a structure.  Each following
% row contains the data for one instance of that structure.
%
%
% This routine writes each element of the structure array as a row.
% Only numeric and string field values are supported.
%
% Open the file
if (isstr(filename))
    fid = fopen(filename,'w+');
else
    fid = filename;
end
if (fid == -1)
    error('Error opening file or invalid fid passed');
end



% write header
theFields = fieldnames(theStructs(1));
nFields = length(theFields);
for i = 1:nFields
    fprintf (fid, '%s', theFields{i});
    if i < nFields
        fprintf (fid, ',');
    else
        fprintf (fid, '\n' );
    end
end

% Now write each struct's data as a line
nStructs = length(theStructs);
for j = 1:nStructs
	for i = 1:nFields	
		if (ischar(getfield(theStructs(j),theFields{i})))
			fprintf(fid,'%s',getfield(theStructs(j),theFields{i}));
		else
			fprintf(fid,'%g',getfield(theStructs(j),theFields{i}));
		end
		if (i < nFields)
			fprintf(fid,',');
		else
			fprintf(fid,'\n');
		end
	end
end

% Close the file.
if (isstr(filename))
    fclose(fid);
end


