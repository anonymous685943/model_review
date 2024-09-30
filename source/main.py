from run_experiment import run_experiment

# STIMULI PARAMETERS
exp_type = "number_estimation"  # "number_estimation", "number_comparison"
individuals = 100  # Number of simulated individuals
stimuli = 40  # Int. (e.g., "40" --> 1-40) or vec. (e.g., [1,5,10])
repetitions = 1  # Number of repetitions for each item / individual
max_compare = 50  # In comparison study: Max quantity of control images
radius = 10  # Radius of objects in pixels
minimum_distance = 0.05  # Min dist between objects. 2=whole image.
radius_distribution = "random"  # "const" (same size), "random" (diff.  size)
use_icon = "dots"  # "dots", "icons" or a file name in the icons folder
object_distribution = "uniform"  # "uniform", "clustered", "homogeneous"

# MODEL PARAMETERS
memory_images = [1, 2]  # Images in LTM...
memory_labels = [1, 2]  # ... and their labels
stm_images = []  # Images in STM...
stm_labels = []  # ... and their labels
iconic_memory_and_stim = []  # Iconic images in LTM & Stimuli
transformation = True  # Ability to pre-process images
memory_limit = 7  # STM size limit
tau = 0.97;  # Human estimates: 100ms = 0.97; 500ms = 1.41, 1000m = 1.38
alpha = 12.55  # Human estimates: 100ms =  12.55; 500ms =  20.95; 1000ms =  25.49

# OUTPUT FOLDER
filename = "delete"  # Extenstion to folder name.

run_experiment(exp_type,
               transformation,
               radius,
               radius_distribution,
               stimuli,
               repetitions,
               use_icon,
               individuals,
               filename,
               memory_images,
               memory_labels,
               iconic_memory_and_stim,
               tau,
               alpha,
               memory_limit,
               stm_images,
               stm_labels,
               max_compare,
               minimum_distance,
               object_distribution
               )
