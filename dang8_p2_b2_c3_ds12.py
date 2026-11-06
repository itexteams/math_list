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


def bt_dang8_p2_b2_c3_ds12(self):
            # Khai báo biến
            xa=randint(1,9)
            ya=xa 
            za=0 
            k=randint(1,9)
            a=k*100
            #b=604
            v0=a
            t0=randint(7,9)
            t1=randint(2,4)
            t2=randint(5,6)
            #be_ta=Rational((b-a*t1)*2,t1**2)
            be_ta=randint(2,6)
            b=a*t1+be_ta*Rational(t1**2,2)

            ab=Rational(be_ta*t2**2,2)+a*t2

            xb=ab/2+xa
            kq=xb+1
            # Nội dung câu hỏi
            noidungcauhoi = ('''Mô hình toán học sau đây được sử dụng trong quan sát chuyển động của một vật. Trong không gian cho hệ tọa độ $Oxyz$, có $\\vec{i}, \\vec{j}, \\vec{k}$ lần lượt là các vectơ đơn vị trên các trục $Ox, Oy, Oz$ và độ dài của mỗi vectơ đơn vị đó bằng $1$ mét. Cho hai điểm $A$ và $B$, trong đó điểm $A$ có tọa độ là $(%s;%s;%s)$. Một vật (coi như là một hạt) chuyển động thẳng với tốc độ phụ thuộc thời gian $t$ (giây) theo công thức $v(t)=\\beta t+%s$ (m/s), trong đó $\\beta$ là hằng số dương và $0 \\le t \\le %s$. Ở thời điểm ban đầu $(t=0)$, vật đi qua $A$ với tốc độ $%s$ m/s và hướng tới $B$. Sau $%s$ giây kể từ thời điểm ban đầu, vật đi được quãng đường $%s$ m. Gọi $\\vec{u}=(a;b;c)$ là vectơ cùng hướng với vectơ $\\vec{AB}$. Biết rằng $\\left| \\vec{u} \\right|=1$ và góc giữa vectơ $\\vec{u}$ lần lượt với các vectơ $\\vec{i}, \\vec{j}, \\vec{k}$ có số đo tương ứng bằng $60^\\circ, 60^\\circ, 45^\\circ$.'''
                            %(latex(xa),latex(ya),latex(za),latex(a),latex(t0),latex(v0),latex(t1),latex(b)
                                ))

            ######################################################################## Nhận biết ############################################
            # Các đáp án
            nb_da_1_d = '\\True $a=\\cos 60^\\circ$'
            nb_da_1_d1 = '\\True $b=\\cos 60^\\circ$'
            nb_da_1_d2 = '\\True $c=\\cos 45^\\circ$'
            nb_da_1_s = '$a=\\cos 45^\\circ$'
            nb_da_1_s1 = '$b=\\cos 45^\\circ$'
            nb_da_1_s2 = '$c=\\cos 60^\\circ$'
            list_nb_da_1=[nb_da_1_d,nb_da_1_s,nb_da_1_d1,nb_da_1_s1,nb_da_1_d2,nb_da_1_s2]
            nb_da_1=random.choice(list_nb_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_nb_1 = [nb_da_1]

            # Nội dung lời giải
            loigiai_nb_1 = ('''Đặt $\\vec{u}=\\vec{OE}=(a;b;c)$ và $\\left| \\vec{u} \\right|=OE=1$ và góc giữa vectơ $\\vec{u}$ với các vectơ $\\vec{i}, \\vec{j}, \\vec{k}$ có số đo tương ứng bằng $60^\\circ, 60^\\circ, 45^\\circ$ suy ra $\\widehat{AOE}=60^\\circ, \\widehat{COE}=60^\\circ, \\widehat{GOE}=45^\\circ$ như hình vẽ sau
                            \\begin{center}
                \\begin{tikzpicture}[line join=round, line cap=round,>=stealth,thick] 
                    \\clip(-2.72,-2.36) rectangle (4.74,3.38);
                    \\draw [line width=1.pt,dash pattern=on 2pt off 2pt] (0.,0.)-- (-1.,-1.);
                    \\draw [line width=1.pt] (-1.,-1.)-- (2.,-1.);
                    \\draw [line width=1.pt] (2.,-1.)-- (3.,0.);
                    \\draw [line width=1.pt,dash pattern=on 2pt off 2pt] (3.,0.)-- (0.,0.);
                    \\draw [line width=1.pt,dash pattern=on 2pt off 2pt] (0.,0.)-- (0.,2.);
                    \\draw [line width=1.pt] (0.,2.)-- (3.,2.);
                    \\draw [line width=1.pt] (3.,2.)-- (3.,0.);
                    \\draw [line width=1.pt] (3.,2.)-- (2.,1.);
                    \\draw [line width=1.pt] (2.,1.)-- (-1.,1.);
                    \\draw [line width=1.pt] (-1.,1.)-- (0.,2.);
                    \\draw [line width=1.pt] (-1.,1.)-- (-1.,-1.);
                    \\draw [line width=1.pt] (2.,1.)-- (2.,-1.);
                    \\draw [line width=1.pt,dash pattern=on 2pt off 2pt] (0.,0.)-- (2.,1.);
                    \\draw [->,line width=1.pt] (-1.,-1.) -- (-2.,-2.);
                    \\draw [->,line width=1.pt] (3.,0.) -- (4.,0.);
                    \\draw [->,line width=1.pt] (0.,2.) -- (0.,3.);
                    \\draw [line width=1.pt] (0.,2.)-- (2.,1.);
                    \\draw [line width=1.pt] (2.,1.)-- (3.,0.);
                    \\draw [line width=1.pt] (2.,1.)-- (-1.,-1.);
                    \\draw (-0.6,0.4) node[anchor=north west] {$O$};
                    \\draw (2.82,0.1) node[anchor=north west] {$C$};
                    \\draw (1.88,-0.8) node[anchor=north west] {$B$};
                    \\draw (-1.5,-0.6) node[anchor=north west] {$A$};
                    \\draw (3.,2.5) node[anchor=north west] {$D$};
                    \\draw (1.72,1.6) node[anchor=north west] {$E$};
                    \\draw (-1.44,1.5) node[anchor=north west] {$F$};
                    \\draw (-0.6,2.5) node[anchor=north west] {$G$};
                    \\draw (3.86,0.2) node[anchor=north west] {$y$};
                    \\draw (-2.26,-1.3) node[anchor=north west] {$x$};
                    \\draw (-0.42,3.1) node[anchor=north west] {$z$};
                \\end{tikzpicture}
            \\end{center}
            Suy ra \\\\
                $a=OA=OE \\cdot \\cos 60^\\circ=\\cos 60^\\circ=\\frac{1}{2}$. \\\\
                    $b=OC=OE \\cdot \\cos 60^\\circ=\\cos 60^\\circ=\\frac{1}{2}$. \\\\
                        $c=OG=OE \\cdot \\cos 45^\\circ=\\cos 45^\\circ=\\frac{\\sqrt{2}}{2}$. \\\\'''
                        %(
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
            th_da_1_d = '\\True Phương trình đường thẳng $AB$ là $\\frac{x-%s}{1}=\\frac{y-%s}{1}=\\frac{z}{\\sqrt{2}}$'%(latex(xa),latex(ya))
            th_da_1_s = 'Phương trình đường thẳng $AB$ là $\\frac{x+%s}{1}=\\frac{y+%s}{1}=\\frac{z}{\\sqrt{2}}$'%(latex(xa),latex(ya))
            list_th_da_1=[th_da_1_d,th_da_1_s]
            th_da_1=random.choice(list_th_da_1)


            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_th_1 = [th_da_1]

            # Nội dung lời giải
            loigiai_th_1 = ('''Ta có $\\vec{u}=\\left(\\frac{1}{2}; \\frac{1}{2}; \\frac{\\sqrt{2}}{2} \\right)$. \\\\
                            Vectơ $\\vec{AB}$ cùng hướng với $\\vec{u}$ nên đường thẳng $AB$ có một vectơ chỉ phương là $(1;1;\\sqrt{2})$. \\\\
                                Phương trình đường thẳng $AB$ là $\\frac{x-%s}{1}=\\frac{y-%s}{1}=\\frac{z}{\\sqrt{2}}$.'''       
                        %(latex(xa),latex(ya)
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
            vd_da_1_d = '\\True $\\beta=%s$' %(latex(be_ta))
            vd_da_1_d1 = '\\True $v(t)=%st+%s$' %(latex(be_ta),latex(a))
            vd_da_1_s = '$\\beta=%s$' %(latex(be_ta+1))
            vd_da_1_s1 = '$v(t)=%st+%s$' %(latex(be_ta+1),latex(a))
            list_vd_da_1=[vd_da_1_d,vd_da_1_s,vd_da_1_d1,vd_da_1_s1]
            vd_da_1=random.choice(list_vd_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vd_1 = [vd_da_1]

            # Nội dung lời giải
            loigiai_vd_1 = ('''Quãng đường đi được trong $%s$ giây là \\\\
                            $s=\\int \\limits_{0}^{%s} \\left| v(t) \\right| \\text{d}t=\\int \\limits_{0}^{%s} \\left( \\beta t+%s \\right) \\text{d}t=%s \\Leftrightarrow \\beta=%s$.\\\\
                                Suy ra $v(t)=%s t+%s$ m/s.'''  
                        %(latex(t1),latex(t1),latex(t1),latex(a),latex(b),latex(be_ta),
                        latex(be_ta),latex(a)
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
            vdc_da_1_d = '\\True Giả sử sau $%s$ giây kể từ thời điểm ban đầu, vật đến điểm $B(x_B;y_B;z_B)$. Khi đó $x_B<%s$' %(latex(t2),latex(kq))
            vdc_da_1_s = 'Giả sử sau $%s$ giây kể từ thời điểm ban đầu, vật đến điểm $B(x_B;y_B;z_B)$. Khi đó $x_B>%s$' %(latex(t2),latex(kq))
            list_vdc_da_1=[vdc_da_1_d,vdc_da_1_s]
            vdc_da_1=random.choice(list_vdc_da_1)
            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vdc_1 = [vdc_da_1]

            # Nội dung lời giải
            loigiai_vdc_1 = ('''Quãng đường đi được trong $%s$ giây là $AB=\\int \\limits_{0}^{%s} \\left| v(t) \\right| \\text{d}t=\\int \\limits_{0}^{%s} \\left( %st+%s \\right) \\text{d}t=%s$ m.\\\\
                            Suy ra $\\vec{AB}=\\frac{AB}{\\left| \\vec{u} \\right|} \\cdot \\vec{u}=\\frac{%s}{1} \\cdot \\left(\\frac{1}{2}; \\frac{1}{2}; \\frac{\\sqrt{2}}{2} \\right) \\Rightarrow x_B=\\frac{%s}{2}+%s=%s<%s$.'''
                        %(latex(t2),latex(t2),
                        latex(t2),latex(be_ta),latex(a),latex(ab),
                        latex(ab),latex(ab),latex(xa),latex(xb),latex(kq)
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
                '\\end{ex}\n \\end{minipage} \n\n').replace('phtr', '\\%')
            return content

