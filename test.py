import click

@click.command()
@click.option('-i1', '--input1', default = 1, type = int)
@click.option('-i2', '--input2', default = 5, type = int)
@click.option('-v', '--init', default = 2, type = int)
def main(init, input1, input2):

    if input1 < 1: return 0
    if input2 < 1: return 0

    vals = [init]
    
    num_ts = 1
    for nt in range(input1):
        num_tr = (vals[nt] + 1) % input2
        vals += [val for val in range(num_tr)]
        num_ts += num_tr
    num_ts -= input1
    
    print(vals)
    print(num_ts)

if __name__ == "__main__":
    main()
