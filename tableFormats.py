from prettytable import PrettyTable
import abc

class TableString(object):
    """Metaclass for formatted table strings."""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod    
    def __unicode__(self): return

    @abc.abstractmethod    
    def __str__(self): return
    
    @abc.abstractmethod
    def get_string(self,outfile,**kwargs):
        '''return the string'''
        return


class latexTable(TableString):
    """Construct and export a LaTeX table from a PrettyTable.

    latexTableExporter(table,**kwargs)

    Required argument:
    -----------------
    table - an instance of prettytable.PrettyTable

    Optional keyword arguments:
    --------------------------
    caption - string - a caption for the table
    label - string - the latex reference ID
    """
    def __init__(self,table,caption='',label=''):
        self.table = table

        # Construct LaTeX string from table
        s = r'\begin{tabular}' + '\n'
        s = s + r'\centering' + '\n'
        s = s + r'\caption{%s}\label{%s}' %(caption,label)
        s = s + '\n'
        s = s + r'\begin{table}{'
        s = s + ''.join(['c',]*len(self.table.field_names)) + '}'
        s = s + '\n'
        s = s + '&'.join(self.table.field_names)+'\\ \hline'+'\n'
        for i in range(len(self.table._rows)):
            row = [str(itm) for itm in self.table._rows[i]]
            s = s + '&'.join(row)
            if i != len(self.table._rows)-1:
                s = s + '\\'
            s = s + '\n'
            
        s = s + r'\end{table}\end{\tabular}'
        self.tableString = s

    def __str__(self):
        return self.tableString
        
    def __unicode__(self):
        return self.tableString

    def get_string(self):
        return self.tableString
 
if __name__ == "__main__":
    t = PrettyTable(['a','b','c'])
    t.add_row([1,2,3])
    xt = latexTable(t,caption='Testing formatted table string',label='tab:test')
    print '\n'
    print xt
    print '\n'
    print xt.get_string()
    print '\n'
