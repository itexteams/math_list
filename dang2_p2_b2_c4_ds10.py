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


def bt_dang2_p2_b2_c4_ds10(self):
            # Khai báo biến
            lisdang=['1','2']
            dang=random.choice(lisdang)

            if dang=='2':
                # Khai báo biến
                x=symbols('x')
                k=randint(1,5)
                x0=-k
                y0=3*k
                c=2*k

                # Nội dung câu hỏi
                noidungcauhoi = ('\\immini{'
                                'Cho hàm số $y=f(x)$ có đồ thị như hình vẽ'
                                '}{'
                                '''
                                \\scalebox{0.7}{ 
                                \\begin{tikzpicture}[line join=round, line cap=round,>=stealth,thick]
                                \\tikzset{every node/.style={scale=0.9}}
                                \\draw[->] (-4.1,0)--(2.1,0) node[below left] {$x$};
                                \\draw[->] (0,-1.1)--(0,4.1) node[below left] {$y$};
                                \\draw (0,0) node [below left] {$O$};
                                \\draw (0,2.1) node [right] {$%s$};
                                \\foreach \\x/\\nx in {-1/%s}
                                    \\draw[thin] (\\x,1pt)--(\\x,-1pt) node [below] {$\\nx$};
                                \\foreach \\y/\\ny in {3/%s}
                                    \\draw[thin] (1pt,\\y)--(-1pt,\\y) node [right] {$\\ny$};
                                \\draw[dashed,thin](-1,0)--(-1,3)--(0,3);
                                \\begin{scope}
                                \\clip (-4,-1) rectangle (2,4);
                                \\draw[samples=200,domain=-4:2,smooth,variable=\\x] plot (\\x,{-1*(\\x)^2+-2*(\\x)+2});
                                \\end{scope}
                                \\end{tikzpicture}}
                                '''
                                '}'
                                %(latex(c),latex(x0),latex(y0)
                                ))

                ######################################################################## Nhận biết ############################################
                # Các đáp án
                nb_da_1_d = '\\True Tọa độ đỉnh của đồ thị hàm số là $\\left(%s; %s \\right)$' %(latex(x0),latex(y0))
                nb_da_1_s = 'Tọa độ đỉnh của đồ thị hàm số là $\\left(%s; %s \\right)$' %(latex(x0),latex(y0+1))
                list_nb_da_1=[nb_da_1_d,nb_da_1_s]
                nb_da_1=random.choice(list_nb_da_1)

                nb_da_2_d = '\\True Giá trị lớn nhất hàm số là $%s$'%(latex(y0))
                nb_da_2_s = 'Giá trị lớn nhất hàm số là $%s$'%(latex(y0+1))
                list_nb_da_2=[nb_da_2_d,nb_da_2_s]
                nb_da_2=random.choice(list_nb_da_2)

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_nb_1 = [nb_da_1,nb_da_2]

                # Nội dung lời giải
                loigiai_nb_1 = ('Từ đồ thị hàm số ta có \\\\ \n'
                        'Tọa độ đỉnh của đồ thị hàm số là $\\left(%s; %s \\right)$.'
                        %(
                            latex(x0),latex(y0)

                        ))
                loigiai_nb_2 = ('Từ đồ thị hàm số ta có \\\\ \n'
                        'Tọa độ đỉnh của đồ thị hàm số là $\\left(%s; %s \\right)$. \\\\ \n'
                        'Vậy giá trị lớn nhất của hàm số là $%s$.'
                        %(
                            latex(x0),latex(y0),
                            latex(y0)

                        ))
                # Đưa các lời giải vào danh sách lời giải
                list_nb_2 = [loigiai_nb_1,loigiai_nb_2]

                # Kết hợp các đáp án và lời giải vào cùng một danh sách
                combined_nb = list(zip(list_nb_1, list_nb_2))

                # Xáo trộn danh sách kết hợp
                random.shuffle(combined_nb)

                # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
                shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)

                ######################################################################## Thông hiểu ############################################
                # Các đáp án
                th_da_1_d = '\\True Đường thẳng $x=%s$ là trục đối xứng của đồ thị hàm số' %(latex(x0))  
                th_da_1_s = 'Đường thẳng $x=%s$ là trục đối xứng của đồ thị hàm số' %(latex(x0+1))  
                list_th_da_1=[th_da_1_d,th_da_1_s]
                th_da_1=random.choice(list_th_da_1)

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_th_1 = [th_da_1]

                # Nội dung lời giải
                loigiai_th_1 = (
                        'Trục đối xứng của đồ thị hàm số là $x=%s$.'
                        %(
                            latex(x0)

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
                vd_da_1_d = '\\True Đồ thị hàm số cắt trục $Oy$ tại điểm có tọa độ là $(0;%s)$'%(latex(c))
                vd_da_1_s = 'Đồ thị hàm số cắt trục $Oy$ tại điểm có tọa độ là $(0;%s)$' %(latex(c+1))
                list_vd_da_1=[vd_da_1_d,vd_da_1_s]
                vd_da_1=random.choice(list_vd_da_1)

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_vd_1 = [vd_da_1]

                # Nội dung lời giải
                loigiai_vd_1 = ('Đồ thị hàm số cắt trục $Oy$ tại điểm có tọa độ là $(0;%s)$'%(latex(c))
                        )

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
                vdc_da_1_d = '\\True Hàm số nghịch biến trên khoảng $\\left(%s; +\\infty \\right)$'%(latex(x0))
                vdc_da_1_s = 'Hàm số nghịch biến trên khoảng $\\left(-\\infty;%s \\right)$'%(latex(x0))
                list_vdc_da_1=[vdc_da_1_d,vdc_da_1_s]
                vdc_da_1=random.choice(list_vdc_da_1)

                vdc_da_2_d = '\\True Hàm số đồng biến trên khoảng $\\left(-\\infty;%s \\right)$'%(latex(x0))
                vdc_da_2_s = 'Hàm số đồng biến trên khoảng $\\left(%s; +\\infty \\right)$'%(latex(x0))
                list_vdc_da_2=[vdc_da_2_d,vdc_da_2_s]
                vdc_da_2=random.choice(list_vdc_da_2)

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_vdc_1 = [vdc_da_1,vdc_da_2]

                # Nội dung lời giải
                loigiai_vdc_1 = (
                        'Trục đối xứng của đồ thị hàm số là $x=%s$. \\\\ \n'
                        'Suy ra hàm số nghịch biến trên khoảng $\\left(%s; +\\infty \\right)$.'
                        %(
                            latex(x0),latex(x0),

                        ))
                loigiai_vdc_2 = (
                        'Trục đối xứng của đồ thị hàm số là $x=%s$. \\\\ \n'
                        'Suy ra hàm số đồng biến trên khoảng $\\left(-\\infty; %s \\right)$.'
                        %(
                            latex(x0),latex(x0),

                        ))

                # Đưa các lời giải vào danh sách lời giải
                list_vdc_2 = [loigiai_vdc_1,loigiai_vdc_2]

                # Kết hợp các đáp án và lời giải vào cùng một danh sách
                combined_vdc = list(zip(list_vdc_1, list_vdc_2))

                # Xáo trộn danh sách kết hợp
                random.shuffle(combined_vdc)

                # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
                shuffled_answers_vdc, shuffled_solutions_vdc = zip(*combined_vdc)

            if dang=='1':
                # Khai báo biến
                x=symbols('x')
                k=randint(1,5)
                x0=k
                y0=-2*k

                # Nội dung câu hỏi
                noidungcauhoi = ('\\immini{'
                                'Cho hàm số $y=f(x)$ có đồ thị như hình vẽ.'
                                '}{'
                                '''
                                \\scalebox{0.7}{ 
                                \\begin{tikzpicture}[line join=round, line cap=round,>=stealth,thick]
                                    \\tikzset{every node/.style={scale=0.9}}
                                    \\draw[->] (-1.1,0)--(5.1,0) node[below left] {$x$};
                                    \\draw[->] (0,-5.1)--(0,2.1) node[below left] {$y$};
                                    \\draw (0,0) node [below left] {$O$};
                                    \\foreach \\x/\\nx in {2/%s}
                                    \\draw[thin] (\\x,1pt)--(\\x,-1pt) node [above] {$\\nx$};
                                    \\foreach \\y/\\ny in {-4/%s}
                                    \\draw[thin] (1pt,\\y)--(-1pt,\\y) node [left] {$\\ny$};
                                    \\draw[dashed,thin](2,0)--(2,-4)--(0,-4);
                                    \\begin{scope}
                                        \\clip (-1,-5) rectangle (5,2);
                                        \\draw[samples=200,domain=-1:5,smooth,variable=\\x] plot (\\x,{1*(\\x)^2+-4*(\\x)+0});
                                    \\end{scope}
                                \\end{tikzpicture} }
                                '''
                                '}'
                                %(latex(x0),latex(y0)
                                ))

                ######################################################################## Nhận biết ############################################
                # Các đáp án
                nb_da_1_d = '\\True Tọa độ đỉnh của đồ thị hàm số là $\\left(%s; %s \\right)$' %(latex(x0),latex(y0))
                nb_da_1_s = 'Tọa độ đỉnh của đồ thị hàm số là $\\left(%s; %s \\right)$' %(latex(x0),latex(y0-1))
                list_nb_da_1=[nb_da_1_d,nb_da_1_s]
                nb_da_1=random.choice(list_nb_da_1)

                nb_da_2_d = '\\True Giá trị nhỏ nhất hàm số là $%s$'%(latex(y0))
                nb_da_2_s = 'Giá trị nhỏ nhất hàm số là $%s$'%(latex(y0+1))
                list_nb_da_2=[nb_da_2_d,nb_da_2_s]
                nb_da_2=random.choice(list_nb_da_2)

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_nb_1 = [nb_da_1,nb_da_2]

                # Nội dung lời giải
                loigiai_nb_1 = ('Từ đồ thị hàm số ta có \\\\ \n'
                        'Tọa độ đỉnh của đồ thị hàm số là $\\left(%s; %s \\right)$.'
                        %(
                            latex(x0),latex(y0)

                        ))
                loigiai_nb_2 = ('Từ đồ thị hàm số ta có \\\\ \n'
                        'Tọa độ đỉnh của đồ thị hàm số là $\\left(%s; %s \\right)$. \\\\ \n'
                        'Vậy giá trị nhỏ nhất của hàm số là $%s$.'
                        %(
                            latex(x0),latex(y0),
                            latex(y0)

                        ))
                # Đưa các lời giải vào danh sách lời giải
                list_nb_2 = [loigiai_nb_1,loigiai_nb_2]

                # Kết hợp các đáp án và lời giải vào cùng một danh sách
                combined_nb = list(zip(list_nb_1, list_nb_2))

                # Xáo trộn danh sách kết hợp
                random.shuffle(combined_nb)

                # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
                shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)

                ######################################################################## Thông hiểu ############################################
                # Các đáp án
                th_da_1_d = '\\True Đường thẳng $x=%s$ là trục đối xứng của đồ thị hàm số' %(latex(x0))  
                th_da_1_s = 'Đường thẳng $x=%s$ là trục đối xứng của đồ thị hàm số' %(latex(x0+1))  
                list_th_da_1=[th_da_1_d,th_da_1_s]
                th_da_1=random.choice(list_th_da_1)

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_th_1 = [th_da_1]

                # Nội dung lời giải
                loigiai_th_1 = (
                        'Trục đối xứng của đồ thị hàm số là $x=%s$.'
                        %(
                            latex(x0)

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
                vd_da_1_d = '\\True Đồ thị hàm số cắt trục $Oy$ tại điểm có tọa độ là $(0;0)$'
                vd_da_1_s = 'Đồ thị hàm số cắt trục $Oy$ tại điểm có tọa độ là $(0;1)$'
                list_vd_da_1=[vd_da_1_d,vd_da_1_s]
                vd_da_1=random.choice(list_vd_da_1)

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_vd_1 = [vd_da_1]

                # Nội dung lời giải
                loigiai_vd_1 = ('Đồ thị hàm số cắt trục $Oy$ tại điểm có tọa độ là $(0;0)$.'
                        %(
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
                vdc_da_1_d = '\\True Hàm số đồng biến trên khoảng $\\left(%s; +\\infty \\right)$'%(latex(x0))
                vdc_da_1_s = 'Hàm số đồng biến trên khoảng $\\left(-\\infty;%s \\right)$'%(latex(x0))
                list_vdc_da_1=[vdc_da_1_d,vdc_da_1_s]
                vdc_da_1=random.choice(list_vdc_da_1)

                vdc_da_2_d = '\\True Hàm số nghịch biến trên khoảng $\\left(-\\infty;%s \\right)$'%(latex(x0))
                vdc_da_2_s = 'Hàm số nghịch biến trên khoảng $\\left(%s; +\\infty \\right)$'%(latex(x0))
                list_vdc_da_2=[vdc_da_2_d,vdc_da_2_s]
                vdc_da_2=random.choice(list_vdc_da_2)

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_vdc_1 = [vdc_da_1,vdc_da_2]

                # Nội dung lời giải
                loigiai_vdc_1 = (
                        'Trục đối xứng của đồ thị hàm số là $x=%s$. \\\\ \n'
                        'Suy ra hàm số đồng biến trên khoảng $\\left(%s; +\\infty \\right)$.'
                        %(
                            latex(x0),latex(x0),

                        ))
                loigiai_vdc_2 = (
                        'Trục đối xứng của đồ thị hàm số là $x=%s$. \\\\ \n'
                        'Suy ra hàm số nghịch biến trên khoảng $\\left(-\\infty; %s \\right)$.'
                        %(
                            latex(x0),latex(x0),

                        ))

                # Đưa các lời giải vào danh sách lời giải
                list_vdc_2 = [loigiai_vdc_1,loigiai_vdc_2]

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

