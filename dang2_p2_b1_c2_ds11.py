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


def bt_dang2_p2_b1_c2_ds11(self):
            # Khai báo biến
            lisdang=['1','2']
            dang=random.choice(lisdang)
            if dang=='2':
                n=symbols('n')
                a=randint(2,9)
                b=randint(-9,9)
                c=randint(2,9)
                d=randint(-9,9)
                while a*d-b*c>=0:
                    a=randint(2,9)
                    b=randint(-9,9)
                    c=randint(2,9)
                    d=randint(-9,9)
                u=(a*n+b)/(c*n+d)

                u1=Rational(a*1+b,c*1+d)
                u2=Rational(a*2+b,c*2+d)
                u3=Rational(a*3+b,c*3+d)

                n0=randint(5,20)
                u0=Rational(a*n0+b,c*n0+d)

                un=(a*(n+1)+b)/(c*(n+1)+d)

                uk=(a*d-b*c)/((c*(n+1)+d)*(c*n+d))
                # Nội dung câu hỏi
                noidungcauhoi = ('''Cho dãy số $(u_n)$ với $u_n=%s$, $n \\in \\mathbb{N}^*$.'''                 
                                %(latex(u)
                                    ))

                ######################################################################## Nhận biết ############################################
                # Các đáp án
                nb_da_1_d = '\\True Ba số hạng đầu của dãy số là $%s; %s; %s$' %(latex(u1),latex(u2),latex(u3))
                nb_da_1_s = 'Ba số hạng đầu của dãy số là $%s; %s; %s$' %(latex(u1),latex(u2),latex(u3+1))
                list_nb_da_1=[nb_da_1_d,nb_da_1_s]
                nb_da_1=random.choice(list_nb_da_1)

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_nb_1 = [nb_da_1]

                # Nội dung lời giải
                loigiai_nb_1 = ('''Ba số hạng đầu của dãy số là $u_1=%s; u_2=%s; u_3=%s$.'''
                            %(latex(u1),latex(u2),latex(u3)
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
                th_da_1_d = '\\True Giá trị $%s$ là số hạng thứ $%s$ của dãy số' %(latex(u0),latex(n0))  
                th_da_1_s = 'Giá trị $%s$ là số hạng thứ $%s$ của dãy số' %(latex(u0),latex(n0+1))  
                list_th_da_1=[th_da_1_d,th_da_1_s]
                th_da_1=random.choice(list_th_da_1)


                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_th_1 = [th_da_1]

                # Nội dung lời giải
                loigiai_th_1 = ('''Ta có \\\\
                                $u_n=%s \\Leftrightarrow %s=%s \\Leftrightarrow n=%s$. \\\\
                                Vậy giá trị $%s$ là số hạng thứ $%s$ của dãy số.'''       
                            %(latex(u0),latex(u),latex(u0),latex(n0),
                            latex(u0),latex(n0)
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
                vd_da_1_d = '\\True Dãy số đã cho là dãy giảm'  
                vd_da_1_s = 'Dãy số đã cho là dãy tăng'  
                list_vd_da_1=[vd_da_1_d,vd_da_1_s]
                vd_da_1=random.choice(list_vd_da_1)

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_vd_1 = [vd_da_1]

                # Nội dung lời giải
                loigiai_vd_1 = ('''Ta có \\\\
                                $u_n=%s, u_{n+1}=%s$. \\\\
                                    Khi đó $u_{n+1}-u_n=\\left(%s\\right)-\\left(%s\\right)=%s<0$ với $n \\in \\mathbb{N}$. \\\\
                                        Vậy dãy số đã cho là dãy số giảm.'''  
                            %(latex(u),latex(un),
                            latex(un),latex(u),latex(uk)
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
                vdc_da_1_d = '\\True Dãy số bị chặn'
                vdc_da_1_s = 'Dãy số bị chặn dưới'
                vdc_da_1_s1 = 'Dãy số bị chặn trên'
                list_vdc_da_1=[vdc_da_1_d,vdc_da_1_s,vdc_da_1_s1]
                vdc_da_1=random.choice(list_vdc_da_1)

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_vdc_1 = [vdc_da_1]

                # Nội dung lời giải
                loigiai_vdc_1 = ('''Dãy số $(u_n)$ là dãy số giảm có $u_1=%s$. Do đó dãy số bị chặn trên tại $%s$.\\\\
                                Mặt khác $u_n=%s+\\frac{%s}{%s} \\ge %s$ với $n \\in \\mathbb{N}$ nên dãy số bị chặn dưới tại $%s$. \\\\
                                    Vậy dãy số đã cho bị chặn.'''
                            %(latex(u1),latex(u1),
                            latex(Rational(a,c)),latex(Rational(b*c-a*d,c)),latex(c*n+d),latex(Rational(a,c)),latex(Rational(a,c))
                                ))

                # Đưa các lời giải vào danh sách lời giải
                list_vdc_2 = [loigiai_vdc_1]

                # Kết hợp các đáp án và lời giải vào cùng một danh sách
                combined_vdc = list(zip(list_vdc_1, list_vdc_2))

                # Xáo trộn danh sách kết hợp
                random.shuffle(combined_vdc)

                # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
                shuffled_answers_vdc, shuffled_solutions_vdc = zip(*combined_vdc)

            if dang=='1':
                n=symbols('n')
                a=randint(2,9)
                b=randint(-9,9)
                c=randint(2,9)
                d=randint(-9,9)
                while a*d-b*c<=0:
                    a=randint(2,9)
                    b=randint(-9,9)
                    c=randint(2,9)
                    d=randint(-9,9)
                u=(a*n+b)/(c*n+d)

                u1=Rational(a*1+b,c*1+d)
                u2=Rational(a*2+b,c*2+d)
                u3=Rational(a*3+b,c*3+d)

                n0=randint(5,20)
                u0=Rational(a*n0+b,c*n0+d)

                un=(a*(n+1)+b)/(c*(n+1)+d)

                uk=(a*d-b*c)/((c*(n+1)+d)*(c*n+d))
                # Nội dung câu hỏi
                noidungcauhoi = ('''Cho dãy số $(u_n)$ với $u_n=%s$, $n \\in \\mathbb{N}^*$.'''                 
                                %(latex(u)
                                    ))

                ######################################################################## Nhận biết ############################################
                # Các đáp án
                nb_da_1_d = '\\True Ba số hạng đầu của dãy số là $%s; %s; %s$' %(latex(u1),latex(u2),latex(u3))
                nb_da_1_s = 'Ba số hạng đầu của dãy số là $%s; %s; %s$' %(latex(u1),latex(u2),latex(u3+1))
                list_nb_da_1=[nb_da_1_d,nb_da_1_s]
                nb_da_1=random.choice(list_nb_da_1)

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_nb_1 = [nb_da_1]

                # Nội dung lời giải
                loigiai_nb_1 = ('''Ba số hạng đầu của dãy số là $u_1=%s; u_2=%s; u_3=%s$.'''
                            %(latex(u1),latex(u2),latex(u3)
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
                th_da_1_d = '\\True Giá trị $%s$ là số hạng thứ $%s$ của dãy số' %(latex(u0),latex(n0))  
                th_da_1_s = 'Giá trị $%s$ là số hạng thứ $%s$ của dãy số' %(latex(u0),latex(n0+1))  
                list_th_da_1=[th_da_1_d,th_da_1_s]
                th_da_1=random.choice(list_th_da_1)


                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_th_1 = [th_da_1]

                # Nội dung lời giải
                loigiai_th_1 = ('''Ta có \\\\
                                $u_n=%s \\Leftrightarrow %s=%s \\Leftrightarrow n=%s$. \\\\
                                Vậy giá trị $%s$ là số hạng thứ $%s$ của dãy số.'''       
                            %(latex(u0),latex(u),latex(u0),latex(n0),
                            latex(u0),latex(n0)
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
                vd_da_1_d = '\\True Dãy số đã cho là dãy tăng'  
                vd_da_1_s = 'Dãy số đã cho là dãy giảm'  
                list_vd_da_1=[vd_da_1_d,vd_da_1_s]
                vd_da_1=random.choice(list_vd_da_1)

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_vd_1 = [vd_da_1]

                # Nội dung lời giải
                loigiai_vd_1 = ('''Ta có \\\\
                                $u_n=%s, u_{n+1}=%s$. \\\\
                                    Khi đó $u_{n+1}-u_n=\\left(%s\\right)-\\left(%s\\right)=%s>0$ với $n \\in \\mathbb{N}$. \\\\
                                        Vậy dãy số đã cho là dãy số tăng.'''  
                            %(latex(u),latex(un),
                            latex(un),latex(u),latex(uk)
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
                vdc_da_1_d = '\\True Dãy số bị chặn'
                vdc_da_1_s = 'Dãy số bị chặn dưới'
                vdc_da_1_s1 = 'Dãy số bị chặn trên'
                list_vdc_da_1=[vdc_da_1_d,vdc_da_1_s,vdc_da_1_s1]
                vdc_da_1=random.choice(list_vdc_da_1)

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_vdc_1 = [vdc_da_1]

                # Nội dung lời giải
                loigiai_vdc_1 = ('''Dãy số $(u_n)$ là dãy số tăng có $u_1=%s$. Do đó dãy số bị chặn dưới tại $%s$.\\\\
                                Mặt khác $u_n=%s+\\frac{%s}{%s} \\le %s$ với $n \\in \\mathbb{N}$ nên dãy số bị chặn trên tại $%s$. \\\\
                                    Vậy dãy số đã cho bị chặn.'''
                            %(latex(u1),latex(u1),
                            latex(Rational(a,c)),latex(Rational(b*c-a*d,c)),latex(c*n+d),latex(Rational(a,c)),latex(Rational(a,c))
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
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

