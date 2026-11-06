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


def bt_dang3_p2_b2_c1_ds12(self):
            # Khai báo biến
            lisdang=['1','2']
            dang=random.choice(lisdang)

            if dang=='2':
                x=symbols('x')
                a=2
                lis1=(0,1,sqrt(2),sqrt(3),2)
                b=random.choice(lis1)
                y=a*cos(x)+b*x
                y0=a*cos(0)+b*0
                ypi=a*cos(pi/2)+b*pi/2

                dh=-a*sin(x)+b
                x0=asin(b/a)
                y1=a*cos(x0)+b*x0

                gtln=max(y0,ypi,y1)
                gtnn=min(y0,ypi,y1)

                # Nội dung câu hỏi
                noidungcauhoi = 'Cho hàm số $f(x)=%s$.' %(latex(y))

                ######################################################################## Nhận biết ############################################
                # Các đáp án
                nb_da_1_d = '\\True $f(0)=%s; f\\left(\\dfrac{\\pi}{2}\\right)=%s$' %(latex(y0),latex(ypi))
                nb_da_1_s = '$f(0)=%s; f\\left(\\dfrac{\\pi}{2}\\right)=%s$' %(latex(y0),latex(ypi+pi))
                list_nb_da_1=[nb_da_1_d,nb_da_1_s]
                nb_da_1=random.choice(list_nb_da_1)


                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_nb_1 = [nb_da_1]

                # Nội dung lời giải
                loigiai_nb_1 = ('Ta có $f(0)=%s; f(\\pi)=%s$.' %(latex(y0),latex(ypi))
                            )

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
                th_da_1_d = '\\True Đạo hàm của hàm số đã cho là $f\'(x)=%s$' %(latex(dh))
                th_da_1_s = 'Đạo hàm của hàm số đã cho là $f\'(x)=%s$' %(latex(dh+1))
                list_th_da_1=[th_da_1_d,th_da_1_s]
                th_da_1=random.choice(list_th_da_1)


                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_th_1 = [th_da_1]

                # Nội dung lời giải
                loigiai_th_1 = ('Đạo hàm của hàm số đã cho là $f\'(x)=%s$.' %(latex(dh))
                            )

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
                vd_da_1_d = '\\True Nghiệm của phương trình $f\'(x)=0$ trên đoạn $\\left[0;\\dfrac{\\pi}{2} \\right]$ là $%s$' %(latex(x0))
                vd_da_1_s = 'Nghiệm của phương trình $f\'(x)=0$ trên đoạn $\\left[0;\\dfrac{\\pi}{2} \\right]$ là $%s$' %(latex(x0+pi))
                list_vd_da_1=[vd_da_1_d,vd_da_1_s]
                vd_da_1=random.choice(list_vd_da_1)

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_vd_1 = [vd_da_1]

                # Nội dung lời giải
                loigiai_vd_1 = ('Ta có \\\\ \n'
                                '\\hspace*{1cm} $f\'(x)=0 \\Leftrightarrow %s=0 \\Leftrightarrow \\sin x =%s \\Leftrightarrow \\hoac{& x= %s+k2\\pi \\\\& x= %s+k2\\pi} (k \\in \\mathbb{Z})$. \\\\ \n'
                                'Ta thấy trên đoạn $\\left[0;\\dfrac{\\pi}{2} \\right]$ phương trình có nghiệm là $x=%s$.'
                                %(latex(dh),latex(b/a),latex(x0),latex(pi-x0),
                                latex(x0)
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
                vdc_da_1_d = '\\True Giá trị lớn nhất của $f(x)$ trên đoạn $\\left[0;\\dfrac{\\pi}{2} \\right]$ là $%s$' %(latex(gtln))
                vdc_da_1_s = 'Giá trị lớn nhất của $f(x)$ trên đoạn $\\left[0;\\dfrac{\\pi}{2} \\right]$ là $%s$' %(latex(gtnn))
                list_vdc_da_1=[vdc_da_1_d,vdc_da_1_s]
                vdc_da_1=random.choice(list_vdc_da_1)

                vdc_da_2_d = '\\True Giá trị nhỏ nhất của $f(x)$ trên đoạn $\\left[0;\\dfrac{\\pi}{2} \\right]$ là $%s$' %(latex(gtnn))
                vdc_da_2_s = 'Giá trị nhỏ nhất của $f(x)$ trên đoạn $\\left[0;\\dfrac{\\pi}{2} \\right]$ là $%s$' %(latex(gtln))
                list_vdc_da_2=[vdc_da_2_d,vdc_da_2_s]
                vdc_da_2=random.choice(list_vdc_da_2)

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_vdc_1 = [vdc_da_1, vdc_da_2]

                # Nội dung lời giải
                loigiai_vdc_1 = ('Ta có \\\\ \n'
                                '\\hspace*{1cm} $f(0)=%s; f\\left(\\dfrac{\\pi}{2}\\right)=%s; f\\left(%s \\right)=%s$. \\\\ \n'
                                'Ta thấy trên đoạn $\\left[0;\\dfrac{\\pi}{2} \\right]$ giá trị lớn nhất của hàm số là $%s$.'
                                %(latex(y0),latex(ypi),latex(x0),latex(y1),
                                latex(gtln)
                                    ))
                loigiai_vdc_2 = ('Ta có \\\\ \n'
                                '\\hspace*{1cm} $f(0)=%s; f\\left(\\dfrac{\\pi}{2}\\right)=%s; f\\left(%s \\right)=%s$. \\\\ \n'
                                'Ta thấy trên đoạn $\\left[0;\\dfrac{\\pi}{2} \\right]$ giá trị nhỏ nhất của hàm số là $%s$.'
                                %(latex(y0),latex(ypi),latex(x0),latex(y1),
                                latex(gtnn)
                                    ))

                # Đưa các lời giải vào danh sách lời giải
                list_vdc_2 = [loigiai_vdc_1, loigiai_vdc_2]

                # Kết hợp các đáp án và lời giải vào cùng một danh sách
                combined_vdc = list(zip(list_vdc_1, list_vdc_2))

                # Xáo trộn danh sách kết hợp
                random.shuffle(combined_vdc)

                # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
                shuffled_answers_vdc, shuffled_solutions_vdc = zip(*combined_vdc)


            if dang=='1':
                x=symbols('x')
                a=2
                lis1=(0,1,sqrt(2),sqrt(3),2,-1,-sqrt(2),-sqrt(3),-2)
                b=random.choice(lis1)
                y=a*sin(x)+b*x
                y0=a*sin(0)+b*0
                ypi=a*sin(pi)+b*pi

                dh=a*cos(x)+b
                x0=acos(-b/a)
                y1=a*sin(x0)+b*x0

                gtln=max(y0,ypi,y1)
                gtnn=min(y0,ypi,y1)

                # Nội dung câu hỏi
                noidungcauhoi = 'Cho hàm số $f(x)=%s$.' %(latex(y))

                ######################################################################## Nhận biết ############################################
                # Các đáp án
                nb_da_1_d = '\\True $f(0)=%s; f(\\pi)=%s$' %(latex(y0),latex(ypi))
                nb_da_1_s = '$f(0)=%s; f(\\pi)=%s$' %(latex(y0),latex(ypi+pi))
                list_nb_da_1=[nb_da_1_d,nb_da_1_s]
                nb_da_1=random.choice(list_nb_da_1)


                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_nb_1 = [nb_da_1]

                # Nội dung lời giải
                loigiai_nb_1 = ('Ta có $f(0)=%s; f(\\pi)=%s$.' %(latex(y0),latex(ypi))
                            )

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
                th_da_1_d = '\\True Đạo hàm của hàm số đã cho là $f\'(x)=%s$' %(latex(dh))
                th_da_1_s = 'Đạo hàm của hàm số đã cho là $f\'(x)=%s$' %(latex(dh+1))
                list_th_da_1=[th_da_1_d,th_da_1_s]
                th_da_1=random.choice(list_th_da_1)


                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_th_1 = [th_da_1]

                # Nội dung lời giải
                loigiai_th_1 = ('Đạo hàm của hàm số đã cho là $f\'(x)=%s$.' %(latex(dh))
                            )

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
                vd_da_1_d = '\\True Nghiệm của phương trình $f\'(x)=0$ trên đoạn $[0;\\pi]$ là $%s$' %(latex(x0))
                vd_da_1_s = 'Nghiệm của phương trình $f\'(x)=0$ trên đoạn $[0;\\pi]$ là $%s$' %(latex(x0+pi))
                list_vd_da_1=[vd_da_1_d,vd_da_1_s]
                vd_da_1=random.choice(list_vd_da_1)

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_vd_1 = [vd_da_1]

                # Nội dung lời giải
                loigiai_vd_1 = ('Ta có \\\\ \n'
                                '\\hspace*{1cm} $f\'(x)=0 \\Leftrightarrow %s=0 \\Leftrightarrow \\cos x =%s \\Leftrightarrow x= \\pm %s+k2\\pi, k \\in \\mathbb{Z}$. \\\\ \n'
                                'Ta thấy trên đoạn $[0;\\pi]$ phương trình có nghiệm là $x=%s$.'
                                %(latex(dh),latex(-b/a),latex(x0),
                                latex(x0)
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
                vdc_da_1_d = '\\True Giá trị lớn nhất của $f(x)$ trên đoạn $[0;\\pi]$ là $%s$' %(latex(gtln))
                vdc_da_1_s = 'Giá trị lớn nhất của $f(x)$ trên đoạn $[0;\\pi]$ là $%s$' %(latex(gtnn))
                list_vdc_da_1=[vdc_da_1_d,vdc_da_1_s]
                vdc_da_1=random.choice(list_vdc_da_1)

                vdc_da_2_d = '\\True Giá trị nhỏ nhất của $f(x)$ trên đoạn $[0;\\pi]$ là $%s$' %(latex(gtnn))
                vdc_da_2_s = 'Giá trị nhỏ nhất của $f(x)$ trên đoạn $[0;\\pi]$ là $%s$' %(latex(gtln))
                list_vdc_da_2=[vdc_da_2_d,vdc_da_2_s]
                vdc_da_2=random.choice(list_vdc_da_2)

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_vdc_1 = [vdc_da_1, vdc_da_2]

                # Nội dung lời giải
                loigiai_vdc_1 = ('Ta có \\\\ \n'
                                '\\hspace*{1cm} $f(0)=%s; f(\\pi)=%s; f\\left(%s \\right)=%s$. \\\\ \n'
                                'Ta thấy trên đoạn $[0;\\pi]$ giá trị lớn nhất của hàm số là $%s$.'
                                %(latex(y0),latex(ypi),latex(x0),latex(y1),
                                latex(gtln)
                                    ))
                loigiai_vdc_2 = ('Ta có \\\\ \n'
                                '\\hspace*{1cm} $f(0)=%s; f(\\pi)=%s; f\\left(%s \\right)=%s$. \\\\ \n'
                                'Ta thấy trên đoạn $[0;\\pi]$ giá trị nhỏ nhất của hàm số là $%s$.'
                                %(latex(y0),latex(pi),latex(x0),latex(y1),
                                latex(gtnn)
                                    ))

                # Đưa các lời giải vào danh sách lời giải
                list_vdc_2 = [loigiai_vdc_1, loigiai_vdc_2]

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
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac').replace('\\left(x \\right)', 'x').replace('1.0471975511966', '\\dfrac{\\pi}{3}').replace('2.0943951023932', '\\dfrac{2 \\pi}{3}').replace('3.14159265358979', '\\pi').replace('0.68485325637228', '\\sqrt{3}-\\dfrac{\\pi}{3}').replace('3.82644590996207', '\\sqrt{3}+\\dfrac{2\\pi}{3}').replace('6.28318530717959', '2\\pi').replace('1.5707963267949', '\\dfrac{\\pi}{2}').replace('0.523598775598299', '\\dfrac{\\pi}{6}').replace('2.25564958316718', '\\sqrt{3}+\\dfrac{\\pi}{6}')
            return content

