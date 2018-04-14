# Obtaining metrics
#
#
#
#
#
#
import mobility as mob

MEAN_LINK_LIFETIME = float()
MEAN_DISTANCE = list()

def medium_distance(nodelist,output_file,MAX_TRANGE,sim_time):
    global MEAN_DISTANCE
    n_nodes = len(nodelist)

    for node in xrange(n_nodes):
          consumer = nodelist[str(node)]
          intervals = sorted(consumer.get_positionDict().keys())
          mean_dist = float()

          for t in intervals:
              if t != '-1' :
                  consumer_pos_at = consumer.get_positionAt(t)
                  for neighbor in xrange(n_nodes):
                      if node != neighbor:
                          producer = nodelist[str(neighbor)]
                          producer_pos_at = producer.get_positionAt(t)
                          if producer_pos_at:
                              distance_fromX = mob.euclidean_distance(a=consumer_pos_at,
                              b=producer_pos_at)
                              if distance_fromX <= MAX_TRANGE:
                                #   print "%s - %d is neighbor of %d" % (t,node,neighbor), consumer_pos_at, producer_pos_at,
                                #   print "distance = %.2f" % (distance_fromX)
                                mean_dist+=distance_fromX
          MEAN_DISTANCE.append(mean_dist/float(sim_time))
    mean = 0.0
    for v in MEAN_DISTANCE:
        mean+=v        
    print mean/n_nodes



# TODO: implement
def medin_lifetime():
    pass
