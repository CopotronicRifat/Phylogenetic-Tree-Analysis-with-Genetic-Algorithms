#Read data from database
from Bio import Entrez
Entrez.email = "rifat11cseruet@gmail.com"

##CHANGE THE PARAMETERS OF THE FOLLOWING LINE TO READ THE EXPECTED DATASET
handle = Entrez.efetch(db="nucleotide", id="EU490707", rettype="gb", retmode="text")
print(handle.read())
for record in records:
    status = record['Entrezgene_track-info']['Gene-track']['Gene-track_status']
    if status.attributes['value']=='discontinued':
        continue
    geneid = record['Entrezgene_track-info']['Gene-track']['Gene-track_geneid']
    genename = record['Entrezgene_gene']['Gene-ref']['Gene-ref_locus']
    print(geneid, genename)


#Build tree from NCBI taxonomy gene database
tree = Phylo.read('ncbi_taxonomy.xml', 'phyloxml')
names = lookup_by_names(tree)
for phylum in ('Apicomplexa', 'Euglenozoa', 'Fungi'):
    print ("Phylum size: %d",len(names[phylum].get_terminals()))

#Get parent from tree
def get_parent(tree, child_clade):
    node_path = tree.get_path(child_clade)
    return node_path[-2]

# Select a clade
myclade = tree.find_clades("parent").next()
# Test the function
parent = get_parent(tree, myclade)
assert myclade in parent

#Create a dictionary mapping all nodes to their parents
def all_parents(tree):
    parents = {}
    for clade in tree.find_clades(order='level'):
        for child in clade:
            parents[child] = clade
    return parents


parents = all_parents(tree)
myclade = tree.find_clades("Tree").next()
parent_of_myclade = parents[myclade]
assert myclade in parent_of_myclade

#Index all parents from trees
def lookup_by_names(tree):
    names = {}
    for clade in tree.find_clades():
        if clade.name:
            if clade.name in names:
                raise ValueError("Duplicate key: %s",clade.name)
            names[clade.name] = clade
    return names

#tabulate representation of species
def tabulate_names(tree):
    names = {}
    for idx, clade in enumerate(tree.find_clades()):
        if clade.name:
            clade.name = ('%d_%s',idx, clade.name)
        else:
            clade.name = str(idx)
        names[clade.name] = clade
    return names


#Calculate distance based method
import itertools

def terminal_neighbor_dists(self):
    def generate_pairs(self):
        pairs = itertools.tee(self)
        pairs[1].next()
        return itertools.izip(pairs[0], pairs[1])
    return [self.distance(*i) for i in
            generate_pairs(self.find_clades(terminal=True))]

#Experimental calculation
import numpy

def to_adjacency_matrix(tree):
    allclades = list(tree.find_clades(order='level'))
    lookup = {}
    for i, elem in enumerate(allclades):
        lookup[elem] = i
    adjmat = numpy.zeros((len(allclades), len(allclades)))
    for parent in tree.find_clades(terminal=False, order='level'):
        for child in parent.clades:
            adjmat[lookup[parent], lookup[child]] = 1
    if not tree.rooted:
        # Branches can go from "child" to "parent" in unrooted trees
        adjmat += adjmat.transpose
    return (allclades, numpy.matrix(adjmat))

def to_distance_matrix(tree):
    allclades = list(tree.find_clades(order='level'))
    lookup = {}
    for i, elem in enumerate(allclades):
        lookup[elem] = i
    distmat = numpy.repeat(numpy.inf, len(allclades)**2)
    distmat.shape = (len(allclades), len(allclades))
    for parent in tree.find_clades(terminal=False, order='level'):
        for child in parent.clades:
            if child.branch_length:
                distmat[lookup[parent], lookup[child]] = child.branch_length
    if not tree.rooted:
        distmat += distmat.transpose
    return (allclades, numpy.matrix(distmat))

#Estimate best phylogenetic tree using Genetic Algorithm
import random
from fuzzywuzzy import fuzz
import string
class Agent:
    def __init__(self, length):
        self.string = ' '.join(random.choice(tree) for _ in xrange(length))
        self.fitness = -1

    def __str__(self):
        return 'Tree: ' + str(self.string) + 'Fitness: ' + str(self.fitness)

in_str = None
in_str_len = None
population = 20
generations = 1000

def GA():
    agents = init_agents(population, in_str_len)
    for generation in xrange(generations):
        print('Generation: '+str(generation))
        agents = fitness(agents)
        agents=selection(agents)
        agents=crossover(agents)
        agents=mutation(agents)

        if any(agent.fitness>=90 for agent in agents):
            print('Threshold value satidfied!')
            exit(0)
    return agents

def init_agents(population, length):
    return [Agent(length for _ in xrange(population))]

def fitness(agents):
    for agent in agents:
        agent.fitness=fuzz.ratio(agent.string, in_str)
    return agents

def selection(agents):
    agents=sorted(agents,key=lamda, agent: agent.fitness, reverse=True)
    print('\n'.join(map(tree, agents)))
    agents=agents[:int(0.2 * len(agents))]
    return agents

def crossover(agents):
    offspring = []
            for _ in xrange((population - len (agents))/2):
                parent1 = random.choice(agents)
                parent2 = random.choice(agents)
                child1=Agent(tree)
                child2=Agent(tree)
                split=random.randint(0,tree)
                child1.string=parent1.string[0:split]+parent2.string[split:in_str_len]
                child2.string=parent2.string[0:split]+parent1.string[split:in_str_len]

                offspring.append(child1)
                offspring.append(child2)
            agents.extend(offspring)
    return agents

def mutation(agents):
    for( agents in agents) :
        for idx, param in enumerate(agent.string):
            if random.uniform(0.0, 1.0)<=0.1:
                agent.string=agent.string[0:idx] + random.choice(string.trees)+agent.string[idx+1:in_str_len]
     return agents

if __name__=='__main__':
    in_str=tree
    in_str_len = len(tree)
    GA()
            

