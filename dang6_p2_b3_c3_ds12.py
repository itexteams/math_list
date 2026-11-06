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


def bt_dang6_p2_b3_c3_ds12(self):
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            # Khai báo biến
            if dang=='1':
                # Khai báo biến
                x=symbols('x')
                a=1 
                b=-4 
                c=5 
                y=a*x**2+b*x+c
                x1=1 
                x2=randint(3,5)
                y1=5

                f=Rational(a,3)*x**3+Rational(b,2)*x**2+c*x
                f1=Rational(a,3)*x1**3+Rational(b,2)*x1**2+c*x1
                f2=Rational(a,3)*x2**3+Rational(b,2)*x2**2+c*x2
                kq=abs(f1-f2)

                r1=a*x1**2+b*x1+c
                r2=a*x2**2+b*x2+c
                while r1>=r2:
                    # Khai báo biến
                    x=symbols('x')
                    a=1 
                    b=-4 
                    c=5 
                    y=a*x**2+b*x+c
                    x1=1 
                    x2=randint(3,5)
                    y1=5

                    f=Rational(a,3)*x**3+Rational(b,2)*x**2+c*x
                    f1=Rational(a,3)*x1**3+Rational(b,2)*x1**2+c*x1
                    f2=Rational(a,3)*x2**3+Rational(b,2)*x2**2+c*x2
                    kq=abs(f1-f2)

                    r1=a*x1**2+b*x1+c
                    r2=a*x2**2+b*x2+c                        
                s1=r1**2
                s2=r2**2
                kq1=s1+s2

                kq3=pi*integrate(y**2, (x, x1, x2))


                # Nội dung câu hỏi
                noidungcauhoi = ('Cho khối tròn xoay như hình vẽ. \n'
                                ''' \\begin{center}
                \\definecolor{zzttqq}{rgb}{0.6,0.2,0.}
                \\scalebox{0.6}{ 
                \\begin{tikzpicture}[line join=round, line cap=round,>=stealth,thick] 
                    \\clip(-1.914381406838122,-6.130491922698069) rectangle (9.5650266064051,5.962319572168825);
                    \\draw[line width=0.8pt,color=zzttqq,fill=zzttqq,pattern=north east lines,pattern color=zzttqq, smooth,samples=50,domain=1.0:4.0] plot(\\x,{\\x^(2.0)-4.0*\\x+5.0}) -- (4.,0.) -- (1.,0.) -- cycle;
                    \\draw[line width=0.8pt,dash pattern=on 4pt off 4pt,color=zzttqq, smooth,samples=50,domain=1.0:4.0] plot(\\x,{0-\\x^(2.0)+4.0*\\x-5.0}) -- (4.,0.) -- (1.,0.) -- cycle;
                    \\draw [samples=50,rotate around={0.:(2.,1.)},xshift=2.cm,yshift=1.cm,line width=1.pt,domain=-4.0:4.0)] plot (\\x,{(\\x)^2/2/0.5});
                    \\draw [->,line width=1.pt] (-1.,0.) -- (6.,0.);
                    \\draw [->,line width=1.pt] (0.,-6.) -- (0.,6.);
                    \\draw [rotate around={90.:(1.,0.)},line width=1.pt,dash pattern=on 4pt off 4pt] (1.,0.) ellipse (2.0075148052028555cm and 0.17353873662290253cm);
                    \\draw [rotate around={90.:(4.,0.)},line width=1.pt,dash pattern=on 4pt off 4pt] (4.,0.) ellipse (5.007549932452432cm and 0.2748751098314152cm);
                    \\draw (-0.6,-0.1) node[anchor=north west] {$O$};
                    \\draw (5.393882931364052,0.09117196234214454) node[anchor=north west] {$x$};
                    \\draw (0.0660355481183424,6) node[anchor=north west] {$y$};
                    \\draw (4.447488988287511,5.7520098070407055) node[anchor=north west] {$y=%s$};
                    \\draw (0.7495422847847327,-0.2) node[anchor=north west] {$%s$};
                    \\draw (3.7289306240997675,-0.2) node[anchor=north west] {$%s$};
                    \\draw (-0.6349970023087246,5.401493531827172) node[anchor=north west] {$%s$};
                \\end{tikzpicture} }
            \\end{center}'''
                                %(latex(y),latex(x1),latex(x2),latex(y1)
                                ))

                ######################################################################## Nhận biết ############################################
                # Các đáp án
                nb_da_1_d = '\\True Hình phẳng (gạch chéo) được giới hạn bởi các đường $y=%s$, trục $Ox$ và hai đường thẳng $x=%s, x=%s$' %(latex(y),latex(x1),latex(x2))
                nb_da_1_s = 'Hình phẳng (gạch chéo) được giới hạn bởi các đường $y=%s$ và hai đường thẳng $x=%s, x=%s$' %(latex(y),latex(x1),latex(x2))
                list_nb_da_1=[nb_da_1_d,nb_da_1_s]
                nb_da_1=random.choice(list_nb_da_1)


                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_nb_1 = [nb_da_1]

                # Nội dung lời giải
                loigiai_nb_1 = ('Từ hình vẽ ta thấy \\\\ \n'
                                'Hình phẳng (gạch chéo) được giới hạn bởi các đường $y=%s$, trục $Ox$ và hai đường thẳng $x=%s, x=%s$.'
                        %(latex(y),latex(x1),latex(x2)
                        ))

                # Đưa các lời giải vào danh sách lời giải
                list_nb_2 = [loigiai_nb_1]

                # Kết hợp các đáp án và lời giải vào cùng một danh sách
                combined_nb = list(zip(list_nb_1, list_nb_2))

                # Xáo trộn danh sách kết hợp
                random.shuffle(combined_nb)

                # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
                shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)

                ######################################################################## Thông hiểu ############################################
                # Các đáp án
                th_da_1_d = '\\True Diện tích hình phẳng là $%s$' %(latex(kq))
                th_da_1_s = 'Diện tích hình phẳng là $%s$' %(latex(kq+1))
                list_th_da_1=[th_da_1_d,th_da_1_s]
                th_da_1=random.choice(list_th_da_1)

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_th_1 = [th_da_1]

                # Nội dung lời giải
                loigiai_th_1 = ('Diện tích hình phẳng là \\\\ \n'
                                '$S=\\displaystyle\\int\\limits_{%s}^{%s} \\left|%s\\right|\\text{d}x=%s$.'
                        %(latex(x1),latex(x2),latex(y),latex(kq)
                        ))


                # Đưa các lời giải vào danh sách lời giải
                list_th_2 = [loigiai_th_1]

                # Kết hợp các đáp án và lời giải vào cùng một danh sách
                combined_th = list(zip(list_th_1, list_th_2))

                # Xáo trộn danh sách kết hợp
                random.shuffle(combined_th)

                # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
                shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)

                ######################################################################## Vận dụng ############################################
                # Các đáp án
                vd_da_1_d = '\\True Tổng diện tích hai đáy của khối tròn xoay là $%s \\pi$' %(latex(kq1))
                vd_da_1_s = 'Tổng diện tích hai đáy của khối tròn xoay là $%s \\pi$' %(latex(kq1-1))
                list_vd_da_1=[vd_da_1_d,vd_da_1_s]
                vd_da_1=random.choice(list_vd_da_1)


                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_vd_1 = [vd_da_1]

                # Nội dung lời giải
                loigiai_vd_1 = (
                        'Bán kính đáy nhỏ của khối tròn xoay là $R_1=%s$ suy ra diện tích đáy nhỏ là $S_1=\\pi R_1^2=%s \\pi$ \\\\ \n'
                        'Bán kính đáy lớn của khối tròn xoay là $R_2=%s$ suy ra diện tích đáy lớn là $S_2=\\pi R_2^2=%s \\pi$ \\\\ \n'
                        'Vậy tổng diện tích hai đáy của khối tròn xoay là $S=S_1+S_2=%s \\pi$.'

                        %(latex(r1),latex(s1),
                        latex(r2),latex(s2),
                        latex(kq1)
                        ))


                # Đưa các lời giải vào danh sách lời giải
                list_vd_2 = [loigiai_vd_1]

                # Kết hợp các đáp án và lời giải vào cùng một danh sách
                combined_vd = list(zip(list_vd_1, list_vd_2))

                # Xáo trộn danh sách kết hợp
                random.shuffle(combined_vd)

                # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
                shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)

                ######################################################################## Vận dụng cao ############################################
                # Các đáp án
                vdc_da_1_d = '\\True Thể tích khối tròn xoay khi quanh hình phẳng quanh trục $Ox$ là $%s$' %(latex(kq3)) 
                vdc_da_1_s = 'Thể tích khối tròn xoay khi quanh hình phẳng quanh trục $Ox$ là $%s$' %(latex(kq3+pi)) 
                list_vdc_da_1=[vdc_da_1_d,vdc_da_1_s]
                vdc_da_1=random.choice(list_vdc_da_1)


                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_vdc_1 = [vdc_da_1]

                # Nội dung lời giải
                loigiai_vdc_1 = ('Thể tích khối tròn xoay khi quanh hình phẳng quanh trục $Ox$ là \\\\ \n'
                        '$S=\\pi \\displaystyle\\int\\limits_{%s}^{%s} \\left(%s\\right)^2 \\text{d}x=%s$.'
                        %(
                            latex(x1),latex(x2),latex(y),latex(kq3)
                        ))

                # Đưa các lời giải vào danh sách lời giải
                list_vdc_2 = [loigiai_vdc_1]

                # Kết hợp các đáp án và lời giải vào cùng một danh sách
                combined_vdc = list(zip(list_vdc_1, list_vdc_2))

                # Xáo trộn danh sách kết hợp
                random.shuffle(combined_vdc)

                # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
                shuffled_answers_vdc, shuffled_solutions_vdc = zip(*combined_vdc)



            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\choiceTFn \n'
                '{'+str(shuffled_answers_nb[0])+'}\n'
                '{'+str(shuffled_answers_th[0])+'}\n'
                '{'+str(shuffled_answers_vd[0])+'}\n'
                '{'+str(shuffled_answers_vdc[0])+'}\n'
                '\\loigiai{ \n'
                '\\begin{enumEX}[a)]{1} \n'
                '\\item '+str(shuffled_solutions_nb[0])+'\n'
                '\\item '+str(shuffled_solutions_th[0])+'\n'
                '\\item '+str(shuffled_solutions_vd[0])+'\n'
                '\\item '+str(shuffled_solutions_vdc[0])+'\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac')
            return content

