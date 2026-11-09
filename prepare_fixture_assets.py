"""Generate original neutral fixtures. Requires Pillow and official FFmpeg."""
from pathlib import Path
import argparse,subprocess,math,json,gzip,shutil
from PIL import Image,ImageDraw

p=argparse.ArgumentParser();p.add_argument('checkout',type=Path);p.add_argument('--ffmpeg',default='ffmpeg');a=p.parse_args()
out=a.checkout/'TMessagesProj/src/main/assets'
if not out.is_dir():p.error('Expected a Telegram Android checkout')
for i in range(6):
 im=Image.new('RGB',(600,600));d=ImageDraw.Draw(im)
 for y in range(600):d.line((0,y,600,y),fill=(int(10+20*i+y*.08),int(18+y*.12),int(55+16*i+y*.06)))
 d.ellipse((70+20*i,80,350+20*i,360),fill=(70+25*i,170,200-20*i))
 d.polygon([(0,600),(230,260+15*i),(600,600)],fill=(20,32+15*i,48+10*i))
 d.text((32,540),f'Original demo image {i+1}',fill='white')
 im.save(out/f'transfer_photo_{i}.jpg',quality=94)
 for name in (['transfer_photo_3_paris_louvre.jpg'] if i==3 else ['transfer_photo_4_paris_notredame.jpg'] if i==4 else []):im.save(out/name,quality=94)
for i in range(3):
 im=Image.new('RGB',(512,512),(18+20*i,30,60+30*i));d=ImageDraw.Draw(im)
 for r in range(180,20,-20):d.ellipse((256-r,256-r,256+r,256+r),outline=(80+30*i,170,210),width=3)
 d.text((30,35),f'Generated audio {i+1}',fill='white');im.save(out/f'transfer_cover_{i}.jpg',quality=94)
 # Distinct, quiet synthesis. Commercial songs are deliberately not redistributed.
 frequencies=[(110,165,220),(130.81,196,261.63),(146.83,220,293.66)][i]
 expr='+'.join(f'0.016*sin(2*PI*{hz}*t)' for hz in frequencies)
 subprocess.run([a.ffmpeg,'-y','-v','error','-f','lavfi','-i',f'aevalsrc={expr}:s=44100:d={[369,203,217][i]}','-af','afade=t=in:d=1,afade=t=out:st='+str([367,201,215][i])+':d=2','-c:a','aac','-b:a','96k',str(out/f'transfer_track_{i}.m4a')],check=True)
for name,letters in [('music_profile_avatar.png','AV'),('transfer_photo_avatar.png','DO')]:
 im=Image.new('RGB',(256,256),'#193a55');d=ImageDraw.Draw(im);d.ellipse((20,20,236,236),fill='#286b99');d.text((116,120),letters,fill='white');im.save(out/name)
pattern=Image.new('RGBA',(100,100));d=ImageDraw.Draw(pattern);d.ellipse((25,25,75,75),outline='white',width=4);pattern.save(out/'transfer_redo_pattern.webp')
lottie={'v':'5.5.7','fr':30,'ip':0,'op':60,'w':512,'h':512,'nm':'Original demo status','ddd':0,'assets':[],'layers':[{'ddd':0,'ind':1,'ty':4,'nm':'Dot','sr':1,'ks':{'o':{'a':0,'k':100},'r':{'a':0,'k':0},'p':{'a':0,'k':[256,256,0]},'a':{'a':0,'k':[0,0,0]},'s':{'a':0,'k':[100,100,100]}},'ao':0,'shapes':[{'ty':'el','p':{'a':0,'k':[0,0]},'s':{'a':0,'k':[320,320]},'nm':'Circle'},{'ty':'fl','c':{'a':0,'k':[.25,.7,.9,1]},'o':{'a':0,'k':100},'r':1,'nm':'Fill'}],'ip':0,'op':60,'st':0,'bm':0}]}
(out/'transfer_redo_model.tgs').write_bytes(gzip.compress(json.dumps(lottie,separators=(',',':')).encode(),mtime=0))
for lang in ['en','ru']:
 src=Path(__file__).with_name(f'transfer_{lang}.xml')
 if not src.exists():src=Path(__file__).resolve().parents[3]/'telegram-android/TMessagesProj/src/main/assets'/src.name
 shutil.copyfile(src,out/src.name)
print('Generated all neutral fixture assets. Audio differs from the presentation; titles are fixture metadata.')
