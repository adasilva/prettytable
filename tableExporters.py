from prettytable import PrettyTable
import abc


class exporter(object):
    """Metaclass for table exporters."""
    __metaclass__ = abc.ABCMeta
    
    @abc.abstractmethod
    def export(self,outfile,**kwargs):
        '''Export data to a file'''
        return

    @abc.abstractmethod    
    def __unicode__(self): return


class latexTableExporter(exporter):
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
    
    def export(self,filename):
        with open(filename,'w') as f:
            f.write(self.tableString)
        return None
        
 
