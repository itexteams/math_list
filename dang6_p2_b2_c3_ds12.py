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


def bt_dang6_p2_b2_c3_ds12(self):
            # Khai báo biến
            t=symbols('t')
            k=randint(1,9)
            x1=1*k 
            x2=2*k 
            x3=3*k 
            x4=4*k 
            x5=5*k 
            y1=x1
            y2=x2
            y3=x3

            v1=t
            s1=Rational(1,2)*t**2
            s1_x2=Rational(1,2)*x2**2

            v2=y2
            s2=Rational(y2,1)*t
            s2_x2=Rational(y2,1)*x2
            s2_x4=Rational(y2,1)*x4
            s22=s2_x4-s2_x2

            s2_x5=Rational(y2,1)*x5
            s33=s2_x5-s2_x2


            # Nội dung câu hỏi
            noidungcauhoi = ('Hình vẽ sau là đồ thị vận tốc $v(t)$ của một vật ($t=0$ là thời điểm vật bắt đầu chuyển động)zz \n'
                            '''\\begin{center}
                \\definecolor{ffqqqq}{rgb}{1.,0.,0.}
                \\begin{tikzpicture}[line join=round, line cap=round,>=stealth,thick] 
                        \\clip(-1.1693593882420266,-1.2467555857761095) rectangle (6.243099747774296,4.277743872861697);
                        \\draw [->,line width=1.pt] (-1.,0.) -- (6.,0.);
                        \\draw [->,line width=1.pt] (0.,-1.) -- (0.,4.);
                        \\draw [line width=1.pt,color=ffqqqq] (0.,0.)-- (2.,2.);
                        \\draw [line width=1.pt,color=ffqqqq] (2.,2.)-- (5.,2.);
                        \\draw [line width=1.pt,dashed] (2.,2.)-- (0.,2.);
                        \\draw [line width=1.pt,dashed] (2.,2.)-- (2.,0.);
                        \\draw [line width=1.pt,dashed] (5.,2.)-- (5.,0.);
                        \\draw (-0.5484867426611723,0.13436927888334219) node[anchor=north west] {$O$};
                        \\draw (5.457505788059746,0.08368579761143571) node[anchor=north west] {$s$};
                        \\draw (-1,4.024326466502164) node[anchor=north west] {$m/s$};
                        \\draw (0.7946255110443494,0) node[anchor=north west] {$%s$};
                        \\draw (1.7576116552105725,0) node[anchor=north west] {$%s$};
                        \\draw (2.834635632238585,0) node[anchor=north west] {$%s$};
                        \\draw (3.848305257676715,0) node[anchor=north west] {$%s$};
                        \\draw (4.785949661206985,0) node[anchor=north west] {$%s$};
                        \\draw (-0.7,1.401456310681004) node[anchor=north west] {$%s$};
                        \\draw (-0.7,2.402455065801157) node[anchor=north west] {$%s$};
                        \\draw (-0.7,3.3907829506033336) node[anchor=north west] {$%s$};
                \\end{tikzpicture}
            \\end{center}'''
                            %(latex(x1),latex(x2),latex(x3),latex(x4),latex(x5),
                            latex(y1),latex(y2),latex(y3),
                            ))

            ######################################################################## Nhận biết ############################################
            # Các đáp án
            nb_da_1_d = '\\True Vận tốc của vật tại thời điểm $t=%s$ là $v(%s)=%s$ m/s' %(latex(x4),latex(x4),latex(y2))
            nb_da_1_s = 'Vận tốc của vật tại thời điểm $t=%s$ là $v(%s)=%s$ m/s' %(latex(x4),latex(x4),latex(y2+1))
            list_nb_da_1=[nb_da_1_d,nb_da_1_s]
            nb_da_1=random.choice(list_nb_da_1)


            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_nb_1 = [nb_da_1]

            # Nội dung lời giải
            loigiai_nb_1 = ('Từ đồ hình vẽ ta thấy \\\\ \n'
                        'Vận tốc của vật tại thời điểm $t=%s$ là $v(%s)=%s$ m/szz'

                    %(latex(x4),latex(x4),latex(y2)
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
            th_da_1_d = '\\True Quãng đường vật di chuyển trong $%s$ giây đầu tiên là $%s$ m' %(latex(x2),latex(s1_x2))
            th_da_1_s = 'Quãng đường vật di chuyển trong $%s$ giây đầu tiên là $%s$ m' %(latex(x2),latex(s1_x2+1))
            list_th_da_1=[th_da_1_d,th_da_1_s]
            th_da_1=random.choice(list_th_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_th_1 = [th_da_1]

            # Nội dung lời giải
            loigiai_th_1 = ('Phương trình vận tốc vật di chuyển trong $%s$ giây đầu tiên là $v=t$zz \\\\'
                            'Quãng đường vật di chuyển trong $%s$ giây đầu tiên là $s_1=\\displaystyle \\int \\limits_{0}^{%s} v(t) \\text{d}t=\\displaystyle \\int \\limits_{0}^{%s} t \\text{d}t=%s$ mzz'

                    %(latex(x2),
                    latex(x2),latex(x2),latex(x2),latex(s1_x2)
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
            vd_da_1_d = '\\True Quãng đường vật di chuyển từ giây thứ $%s$ đến giây thứ $%s$ là $%s$ m' %(latex(x2),latex(x4),latex(s22))
            vd_da_1_s = 'Quãng đường vật di chuyển từ giây thứ $%s$ đến giây thứ $%s$ là $%s$ m' %(latex(x2),latex(x4),latex(s22-1))
            list_vd_da_1=[vd_da_1_d,vd_da_1_s]
            vd_da_1=random.choice(list_vd_da_1)


            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vd_1 = [vd_da_1]

            # Nội dung lời giải
            loigiai_vd_1 = ('Phương trình vận tốc vật di chuyển từ giây thứ $%s$ đến giây thứ $%s$ là $v=%s$zz \\\\'
                            'Quãng đường vật di chuyển từ giây thứ $%s$ đến giây thứ $%s$ là $s_1=\\displaystyle \\int \\limits_{%s}^{%s} v(t) \\text{d}t=\\displaystyle \\int \\limits_{%s}^{%s} %s \\text{d}t=%s$ mzz'

                    %(latex(x2),latex(x4),latex(y2),
                    latex(x2),latex(x4),latex(x2),latex(x4),latex(x2),latex(x4),latex(y2),latex(s22)
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
            vdc_da_1_d = '\\True Tổng quãng đường vật di chuyển trong $%s$ giây đầu tiên là $%s$ m' %(latex(x5),latex(s1_x2+s33))
            vdc_da_1_s = 'Tổng quãng đường vật di chuyển trong $%s$ giây đầu tiên là $%s$ m' %(latex(x5),latex(s1_x2+s33+2))
            list_vdc_da_1=[vdc_da_1_d,vdc_da_1_s]
            vdc_da_1=random.choice(list_vdc_da_1)


            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vdc_1 = [vdc_da_1]

            # Nội dung lời giải
            loigiai_vdc_1 = (
                            'Quãng đường vật di chuyển từ giây thứ $%s$ đến giây thứ $%s$ là $s_1=\\displaystyle \\int \\limits_{%s}^{%s} v(t) \\text{d}t=\\displaystyle \\int \\limits_{%s}^{%s} %s \\text{d}t=%s$zz \\\\ \n'
                    'Vậy tổng quãng đường vật di chuyển trong $%s$ giây đầu tiên là $%s+%s=%s$ mzz'
                    %(
                    latex(x2),latex(x5),latex(x2),latex(x5),latex(x2),latex(x5),latex(y2),latex(s33),
                    latex(x5),latex(s1_x2),latex(s33),latex(s1_x2+s33)
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
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac').replace('zz', '.').replace('phtr', '\\%').replace('{\\left(', '{').replace('\\right)}', '}')
            return content

