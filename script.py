
    

ambientes = 24
naoexiste = [11,16]

print "lista de ambientes\n\n"

for i in range(1, ambientes + 1):
  if i in naoexiste:
    continue
  print "<div class=\"card\"><button style=\"background: url(../Images/AmbThumbs/"+str(i)+"_tn.png); width: 350px; height: 350px;\" type=\"button\" class=\"btn btn-info\" data-toggle=\"modal\" data-target=\"#myModal"+str(i)+"\"></button><p class=\"card-text\">"+str(i)+"</p></div>"
  
  
print "\n\nlista de imagens\n"
  
imagens = [10,7,8,8,8,5,6,5,3,6,0,7,6,5,9,0,8,8,5,7,7,7,7,6]
print len(imagens)

for o in range(1,ambientes+1):
  if o in naoexiste:
      continue
    
  print "<div class=\"modal fade bs-example-modal-lg\" id=\"myModal"+str(o)+"\" role=\"dialog\"><div class=\"modal-dialog modal-lg\"><div class=\"modal-content\"><div class=\"modal-header\"><button type=\"button\" class=\"close\" data-dismiss=\"modal\">×</button></div><div class=\"modal-body\"><div id=\"myCarousel"+str(o)+"\" class=\"carousel slide carousel-fit\" data-ride=\"carousel\" data-interval=\"60000\" style=\"margin-top: 0px; height: 750px;\"><div class=\"carousel-inner\">"
  
  for i in range(1, imagens[o-1] + 1):
    if i==1:
      print "<div class=\"item active\"><img style=\"margin: 0 auto; height: 100%;\" src=\"../Images/Ambientes/Ambiente" + str(o) + "/"+str(i)+".JPG\"></div>"
    else:
      print "<div class=\"item\"><img style=\"margin: 0 auto; height: 100%;\" src=\"../Images/Ambientes/Ambiente" + str(o) + "/"+str(i)+".JPG\"></div>"
  
  print "</div><a href=\"#myCarousel"+str(o)+"\" class=\"left carousel-control\" data-slide=\"prev\"><span class=\"glyphicon glyphicon-chevron-left\"></span></a><a href=\"#myCarousel"+str(o)+"\" class=\"right carousel-control\"  data-slide=\"next\"><span class=\"glyphicon glyphicon-chevron-right\"></span></a></div></div></div></div></div>"
  