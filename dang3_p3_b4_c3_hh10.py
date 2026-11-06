import sys
from PyQt5.QtWidgets import QApplication, QColorDialog, QMainWindow, QSplitter, QTreeWidget, QSpacerItem, QSizePolicy, QTreeWidgetItem, QCheckBox, QFileDialog, QVBoxLayout, QTextEdit, QPushButton, QWidget, QLabel, QLineEdit, QDialog, QAction, QMessageBox, QScrollBar, QHeaderView, QMenu, QGridLayout
from sympy import *
from sympy.abc import x
import sympy as sp
from sympy import symbols,sqrt,evaluate,Subs,latex, Rational, expand, simplify, integrate
import random
import math
from sympy import Rational
from fractions import Fraction as frac
from random import randint
from PyQt5.QtGui import QTextCursor
from PyQt5.QtGui import QFont
import hashlib
import uuid
import os
from sympy import symbols, Eq, solve
import numpy as np
from PyQt5.QtGui import QIcon
from math import factorial
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QTextDocument
from subprocess import run, CalledProcessError
import shutil
from PyQt5.QtWidgets import QProgressBar
from docx import Document
from PyQt5 import QtGui
import re
import pandas as pd
from PyQt5.QtGui import QPixmap
import subprocess
import platform
import json
from decimal import Decimal, ROUND_HALF_UP
from PyQt5.QtWidgets import QComboBox, QPushButton, QVBoxLayout, QWidget
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QSpinBox, QTreeWidget, QTreeWidgetItem, QCheckBox, QTextEdit, QPushButton, QHBoxLayout
from random import randint, choice, shuffle
from sympy import latex
from fractions import Fraction
from collections import Counter
from random import sample
import shutil
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt
import qrcode
import json
import glob
import os
import platform
import subprocess
import hashlib
import base64
from datetime import datetime, timedelta
from PyQt5.QtWidgets import (QApplication, QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox)
from sympy import symbols, solve, Lt
#from PyQt5.QtWebEngineWidgets import QWebEngineView
#from PyQt5.QtCore import QUrl
#from sympy import latex
import re
import pyperclip
import warnings
warnings.filterwarnings("ignore", category=FutureWarning)

import google.generativeai as genai
from sympy.abc import x, y, z, t
import sys
import os
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QFileDialog, QMessageBox
)
from pdf2image import convert_from_path
from math import degrees
import openpyxl
from openpyxl import Workbook
from openpyxl.styles import Alignment, Font
from openpyxl.utils import get_column_letter
from sympy import simplify, collect
from itertools import combinations
import itertools
from PyQt5.QtCore import QSettings
import sys
import os
import platform
import subprocess
import hashlib
import time
from datetime import datetime, timedelta
# Bổ sung các widget và core cho Splash Screen
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QDialog, QLabel, QLineEdit, 
    QPushButton, QComboBox, QCheckBox, QTextEdit, QVBoxLayout, 
    QHBoxLayout, QGridLayout, QMessageBox, QColorDialog,
    QSplashScreen, QProgressBar  # <-- BỔ SUNG 2 CÁI NÀY
)
from PyQt5.QtCore import Qt, QSettings, QThread, pyqtSignal  # <-- BỔ SUNG QThread, pyqtSignal
from PyQt5.QtGui import QIcon, QPixmap, QFont
from PyQt5.QtGui import QFont, QBrush, QColor
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QSplitter, QTreeWidget, QTreeWidgetItem, QTextEdit, QLabel, 
    QSpacerItem, QSizePolicy, QStackedWidget, QPushButton, QCheckBox, QSpinBox,
    QScrollArea  # <-- Thêm mục này vào đây
)
from PyQt5.QtWidgets import QCheckBox
from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5.QtCore import Qt, QPropertyAnimation, pyqtProperty
from functools import wraps
import re
import uuid
import json, base64
from datetime import datetime
from nacl.signing import VerifyKey
from nacl.encoding import HexEncoder
from nacl.exceptions import BadSignatureError
### CÔNG CỤ
import sys
import numpy as np
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QPushButton, QDialog, 
    QVBoxLayout, QHBoxLayout, QTabWidget, QWidget, 
    QLabel, QSlider, QDoubleSpinBox, QGroupBox
)
from PyQt5.QtCore import Qt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from mpl_toolkits.mplot3d import Axes3D  # Cần cho 3D


def bt_dang3_p3_b4_c3_hh10(self):
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)
            if dang=='1':
                # Khai báo biến
                x = symbols("x")
                y = symbols('y')

                d1 = randint(5,10)
                d=2*d1
                r = randint(3,8)
                k = randint(1,7)

                while r>=d1 or k>=r:
                    x = symbols("x")
                    y = symbols('y')

                    d1 = randint(5,10)
                    d=2*d1
                    r = randint(3,8)
                    k = randint(1,7)

                h1=Rational((r**2*d1**2-r**2*k**2),d1**2)
                h=sqrt(h1)

                number = Decimal(float(h))  # Số cần làm tròn
                kq= number.quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)




                # Câu hỏi
                noidungcauhoi=('''Mái vòm của một đường hầm có hình bán elip (hình minh họa). Chiều rộng của đường hầm là $%s m$, điểm cao nhất của mái vòm là $%s m$. Gọi $h$ là chiều cao của mái vòm tại điểm cách tâm đường hầm $%s m$. Khi đó $h$ bằng bao nhiêu $m$? (Kết quả làm tròn đến hàng phần chục)'''
                            '\\begin{center} \n'
                            ''' \\scalebox{0.6}{
                            \\definecolor{eqeqeq}{rgb}{0.8784313725490196,0.8784313725490196,0.8784313725490196}
            \\definecolor{ttqqqq}{rgb}{0.2,0.,0.}
            \\definecolor{ffffff}{rgb}{1.,1.,1.}
            \\definecolor{ccqqqq}{rgb}{0.8,0.,0.}
            \\begin{tikzpicture}[line cap=round,line join=round,>=triangle 45,x=1.0cm,y=1.0cm]
                \\clip(-6.17560307059983,-0.7) rectangle (5.82809155921451,4);
                \\fill[color=ccqqqq,fill=ccqqqq,fill opacity=0.45] (-5.,0.) -- (-5.,4.) -- (5.,4.) -- (5.,0.) -- cycle;
                \\draw [color=ccqqqq] (-5.,0.)-- (-5.,4.);
                \\draw [color=ccqqqq] (-5.,4.)-- (5.,4.);
                \\draw [color=ccqqqq] (5.,4.)-- (5.,0.);
                \\draw [color=ccqqqq] (5.,0.)-- (-5.,0.);
                \\draw [rotate around={0.:(0.,0.)},color=ffffff,fill=ffffff,fill opacity=1.0] (0.,0.) ellipse (3.4935688431838896cm and 2.864441177972629cm);
                \\draw [dash pattern=on 1pt off 1pt,color=ttqqqq] (-3.4935688431838896,0.)-- (-3.5,3.5);
                \\draw [dash pattern=on 1pt off 1pt,color=ttqqqq] (3.49356884318389,0.)-- (3.5,3.5);
                \\draw [dash pattern=on 1pt off 1pt,color=ttqqqq] (0.,2.8644411779726284)-- (-4.488477139797239,2.8482272187954023);
                \\draw [<->] (-3.5,3.5) -- (3.5,3.5);
                \\draw [<->] (1.4876118587871487,2.624192668075107) -- (1.5,0.);
                \\draw [<->] (0.,-0.5) -- (1.5,-0.5);
                \\draw [dash pattern=on 1pt off 1pt,color=ttqqqq] (1.5,0.)-- (1.5,-0.5);
                \\draw [dash pattern=on 1pt off 1pt,color=ttqqqq] (0.,0.)-- (0.,-0.5);
                \\draw [color=eqeqeq] (-5.,3.)-- (5.,3.);
                \\draw [color=eqeqeq] (-5.,2.)-- (-2.5110535926003115,1.991512813375916);
                \\draw [color=eqeqeq] (2.507322295040508,1.9946707759607145)-- (5.,2.);
                \\draw [color=eqeqeq] (3.270546870389099,1.0070474715424276)-- (5.,1.);
                \\draw [color=eqeqeq] (-5.,1.)-- (-3.27515228578052,0.9969346530865897);
                \\draw [color=eqeqeq] (-3.,4.)-- (-3.,3.);
                \\draw [color=eqeqeq] (-1.,4.)-- (-1.,3.);
                \\draw [color=eqeqeq] (1.,4.)-- (1.,3.);
                \\draw [color=eqeqeq] (3.,4.)-- (3.,3.);
                \\draw [color=eqeqeq] (4.,3.)-- (4.000004570815725,1.997862058271801);
                \\draw [color=eqeqeq] (4.000016605113828,1.0040749034464704)-- (4.,0.);
                \\draw [color=eqeqeq] (3.000009141631451,1.9957241165436017)-- (2.9895957780276565,1.4820668398876213);
                \\draw [color=eqeqeq] (2.,3.)-- (2.0099206696920997,2.342907471519193);
                \\draw [color=eqeqeq] (-2.,3.)-- (-2.00122533528635294,2.3415609989880157);
                \\draw [color=eqeqeq] (-4.,3.)-- (-4.000011627634272,1.9965900881140108);
                \\draw [color=eqeqeq] (-4.000003158321793,0.9982228360180507)-- (-4.,0.);
                \\draw [color=eqeqeq] (-3.000023255268544,1.993180176228022)-- (-2.99583981922356,1.4735661883047173);
                \\draw [<->] (-4.5,0.) -- (-4.488477139797239,2.8482272187954023);
                \\draw (-3.4935688431838896,0.)-- (3.49356884318389,0.);
                \\draw (-0.37192995948676494,3.5) node[anchor=north west] {$%s m$};
                \\draw (-4.5,1.7614498122020859) node[anchor=north west] {$%s m$};
                \\draw (0.40661155541864624,0.006192578597163829) node[anchor=north west] {$%s m$};
                \\draw (1.4,1.7189839113890637) node[anchor=north west] {$h$};
            \\end{tikzpicture}}'''
                            '\\end{center} \n'
                            %(latex(d), latex(r), latex(k),
                                latex(d), latex(r), latex(k)))

                # Nội dung lời giải
                loigiai=( 'Đặt hệ trục $(Oxy)$ như hình vẽ với gốc $O$ trùng với tâm đường hầm.'
                        '\\begin{center} \n'
                            '''\\scalebox{0.6}{
                            \\definecolor{eqeqeq}{rgb}{0.8784313725490196,0.8784313725490196,0.8784313725490196}
            \\definecolor{ttqqqq}{rgb}{0.2,0.,0.}
            \\definecolor{ffffff}{rgb}{1.,1.,1.}
            \\definecolor{ccqqqq}{rgb}{0.8,0.,0.}
            \\begin{tikzpicture}[line cap=round,line join=round,>=triangle 45,x=1.0cm,y=1.0cm]
                \\clip(-6.17560307059983,-0.5) rectangle (7,5);
                \\fill[color=ccqqqq,fill=ccqqqq,fill opacity=0.45] (-5.,0.) -- (-5.,4.) -- (5.,4.) -- (5.,0.) -- cycle;
                \\draw [color=ccqqqq] (-5.,0.)-- (-5.,4.);
                \\draw [color=ccqqqq] (-5.,4.)-- (5.,4.);
                \\draw [color=ccqqqq] (5.,4.)-- (5.,0.);
                \\draw [color=ccqqqq] (5.,0.)-- (-5.,0.);
                \\draw [rotate around={0.:(0.,0.)},color=ffffff,fill=ffffff,fill opacity=1.0] (0.,0.) ellipse (3.4935688431838896cm and 2.864441177972629cm);
                \\draw [color=eqeqeq] (-5.,3.)-- (5.,3.);
                \\draw [color=eqeqeq] (-5.,2.)-- (-2.5110535926003115,1.991512813375916);
                \\draw [color=eqeqeq] (2.507322295040508,1.9946707759607145)-- (5.,2.);
                \\draw [color=eqeqeq] (3.270546870389099,1.0070474715424276)-- (5.,1.);
                \\draw [color=eqeqeq] (-5.,1.)-- (-3.27515228578052,0.9969346530865897);
                \\draw [color=eqeqeq] (-3.,4.)-- (-3.,3.);
                \\draw [color=eqeqeq] (-1.,4.)-- (-1.,3.);
                \\draw [color=eqeqeq] (1.,4.)-- (1.,3.);
                \\draw [color=eqeqeq] (3.,4.)-- (3.,3.);
                \\draw [color=eqeqeq] (4.,3.)-- (4.000004570815725,1.997862058271801);
                \\draw [color=eqeqeq] (4.000016605113828,1.0040749034464704)-- (4.,0.);
                \\draw [color=eqeqeq] (3.000009141631451,1.9957241165436017)-- (2.9895957780276565,1.4820668398876213);
                \\draw [color=eqeqeq] (2.,3.)-- (2.0099206696920997,2.342907471519193);
                \\draw [color=eqeqeq] (-2.,3.)-- (-2.00122533528635294,2.3415609989880157);
                \\draw [color=eqeqeq] (-4.,3.)-- (-4.000011627634272,1.9965900881140108);
                \\draw [color=eqeqeq] (-4.000003158321793,0.9982228360180507)-- (-4.,0.);
                \\draw [color=eqeqeq] (-3.000023255268544,1.993180176228022)-- (-2.99583981922356,1.4735661883047173);
                \\draw (3,0) node[anchor=north west] {$%s m$};
                \\draw (-0.8,3.5) node[anchor=north west] {$%s m$};
                \\draw (1.2,0) node[anchor=north west] {$%s m$};
                \\draw (-0.5,2.7) node[anchor=north west] {$h$};
                \\draw (-0.5,0) node[anchor=north west] {$O$};
                \\draw (5.6,-0.1) node[anchor=north west] {$x$};
                \\draw (-0.5,5) node[anchor=north west] {$y$};
                \\draw [->] (0,0.) -- (6,0);
                \\draw [->] (0,0) -- (0,5);
                \\draw [dash pattern=on 1pt off 1pt,color=ttqqqq] (0,2.5)-- (1.7,2.5);
                \\draw [dash pattern=on 1pt off 1pt,color=ttqqqq] (1.7,2.5)-- (1.7,0);
            \\end{tikzpicture}}'''
                            '\\end{center} \n'
                        'Phương trình đường bán elip có dạng $\\heva{& \\dfrac{x^2}{%s^2}+\\dfrac{y^2}{%s^2}=1 \\\\ & y\\ge0}$.\\\\ \n'
                        'Điểm cách tâm đường hầm $%s m$ thì $h$ là tung độ của hình bán elip với $x=%s$.\\\\ \n'
                        'Khi đó $\\heva{& \\dfrac{%s^2}{%s^2}+\\dfrac{h^2}{%s^2}=1 \\\\ & h\\ge0}\\Rightarrow h=%s \\approx %s$'


                        %(latex(d1), latex(r), latex(k),
                            latex(d1),latex(r),
                            latex(k),latex(k),
                            latex(k),latex(d1),latex(r),latex(h),latex(kq),

                            ))


                #Đáp án
                dapan='  \\shortans[0]{$%s$}   \n'%(latex(kq))

            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+str(dapan)+
                '\\loigiai{ \n'
                +str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac').replace('- +','-').replace('+ -', '-').replace('- -', '+').replace('.00', 'zzz').replace('.0', '').replace('zzz', '.00')
            return content 

