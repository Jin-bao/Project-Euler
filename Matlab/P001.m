providedNum = 1000;
mtpList = [];
for i = 1:providedNum-1
  if mod(i,3) == 0
    mtpList = [mtpList i];
  end
  if mod(i,5)==0 && mod(i,3)~=0
    mtpList = [mtpList i];
  end
end
sum(mtpList)