""" Convert direction, time of day and day of year into vectors """

# Convert degrees to radians
  pi = tf.constant(m.pi)
  wd_rad = inputs['wd (deg)'] * pi / 180.0

  # Calculate the wind x and y components.
  outputs['Wx'] = inputs['wv (m/s)'] * tf.math.cos(wd_rad)
  outputs['Wy'] = inputs['wv (m/s)'] * tf.math.sin(wd_rad)

  # Delete `wv (m/s)` and `wd (deg)` after getting the wind vector
  del outputs['wv (m/s)']
  del outputs['wd (deg)']

  # Get day and year in seconds
  day = tf.cast(24*60*60, tf.float32)
  year = tf.cast((365.2425)*day, tf.float32)

  # Get timestamp feature
  timestamp_s = outputs['Date Time']

  # Convert timestamps into periodic signals
  outputs['Day sin'] = tf.math.sin(timestamp_s * (2 * pi / day))
  outputs['Day cos'] = tf.math.cos(timestamp_s * (2 * pi / day))
  outputs['Year sin'] = tf.math.sin(timestamp_s * (2 * pi / year))
  outputs['Year cos'] = tf.math.cos(timestamp_s * (2 * pi / year))
