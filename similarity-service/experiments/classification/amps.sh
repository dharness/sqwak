for f in UrbanSound8K/audio/**/*.wav
do
  fname=$(basename $f)
  ffmpeg -i $f -acodec pcm_f32le -ar 96000 UrbanSound8K/formatted_audio/$fname
done
