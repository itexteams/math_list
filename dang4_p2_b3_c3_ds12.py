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


def bt_dang4_p2_b3_c3_ds12(self):
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            # Khai báo biến
            if dang=='1':
                # Khai báo biến
                x=symbols('x')
                x1=randint(-3,0)
                x2=randint(1,3)
                m=randint(1,9)

                f=x**2-(x1+x2)*x+x1*x2

                f1=(m+1)*x**2-(x1+x2+m)*x+x1*x2-m
                f2=m*x**2-m*x-m

                a=x2+1 
                b=a+2

                y=Rational(1,3)*x**3-Rational(x1+x2,2)*x**2+x1*x2*x

                fa=Rational(1,3)*a**3-Rational(x1+x2,2)*a**2+x1*x2*a
                fx2=Rational(1,3)*x2**3-Rational(x1+x2,2)*x2**2+x1*x2*x2
                fb=Rational(1,3)*b**3-Rational(x1+x2,2)*b**2+x1*x2*b
                kq=abs(fb-fa)

                fx1=Rational(1,3)*x1**3-Rational(x1+x2,2)*x1**2+x1*x2*x1

                f1x1=Rational(m+1,3)*x1**3-Rational(x1+x2+m,2)*x1**2+(x1*x2-m)*x1
                f1x2=Rational(m+1,3)*x2**3-Rational(x1+x2+m,2)*x2**2+(x1*x2-m)*x2
                kq2=abs(f1x1-f1x2)


                # Nội dung câu hỏi
                noidungcauhoi = ('Gọi H là hình phẳng giới hạn bởi các đồ thị hàm số $f(x)=%s; g(x)=%s$ và hai đường thẳng $x=%s, x=%s$$zz$'
                                %(latex(f1),latex(f2),latex(a),latex(b)
                                ))

                ######################################################################## Nhận biết ############################################
                # Các đáp án
                nb_da_1_d = '\\True Phương trình $f(x)=g(x)$ không có nghiệm thuộc đoạn $[%s;%s]$' %(latex(a),latex(b))
                nb_da_1_s = 'Phương trình $f(x)=g(x)$ có hai nghiệm thuộc đoạn $[%s;%s]$' %(latex(a),latex(b))
                list_nb_da_1=[nb_da_1_d,nb_da_1_s]
                nb_da_1=random.choice(list_nb_da_1)


                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_nb_1 = [nb_da_1]

                # Nội dung lời giải
                loigiai_nb_1 = ('Ta có \\\\ \n'
                        '\\hspace*{1cm} $%s=%s \\Leftrightarrow %s=0 \\Leftrightarrow \\hoac{& x=%s \\\\ & x=%s}$$zz$ \\\\ \n'
                        'Các nghiệm của phương trình không thuộc đoạn $\\left[%s; %s \\right]$$zz$'
                        %(latex(f1),latex(f2),latex(f),latex(x1),latex(x2),
                        latex(a),latex(b),
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
                th_da_1_d = '\\True Diện tích của H được tính theo công thức $S=\\displaystyle\\int\\limits_{%s}^{%s} \\left|%s\\right|\\text{d}x$' %(latex(a),latex(b),latex(f))
                th_da_1_s = 'Diện tích của H được tính theo công thức $S=\\pi \\displaystyle\\int\\limits_{%s}^{%s} \\left(%s\\right)^2 \\text{d}x$' %(latex(a),latex(b),latex(f))
                list_th_da_1=[th_da_1_d,th_da_1_s]
                th_da_1=random.choice(list_th_da_1)

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_th_1 = [th_da_1]

                # Nội dung lời giải
                loigiai_th_1 = (
                        'Diện tích hình H được tính theo công thức $S=\\displaystyle\\int\\limits_{%s}^{%s} \\left|%s\\right|\\text{d}x$$zz$'
                        %(
                            latex(a),latex(b),latex(f)
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
                vd_da_1_d = '\\True Diện tích hình phẳng H là $%s$' %(latex(kq))
                vd_da_1_s = 'Diện tích hình phẳng H là $%s$' %(latex(kq+1))
                list_vd_da_1=[vd_da_1_d,vd_da_1_s]
                vd_da_1=random.choice(list_vd_da_1)


                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_vd_1 = [vd_da_1]

                # Nội dung lời giải
                loigiai_vd_1 = (
                        'Suy ra \\\\ \n'
                        'Diện tích hình phẳng cần tìm là $S=\\displaystyle\\int\\limits_{%s}^{%s} \\left|%s\\right|\\text{d}x=%s$$zz$'
                        %(
                            latex(a),latex(b),latex(f),latex(kq)
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
                vdc_da_1_d = '\\True Diện tích hình phẳng giới hạn bởi đồ thị hàm số $y=f(x)$ với trục $Ox$ trên đoạn $[%s;%s]$ là $%s$' %(latex(x1),latex(x2),latex(kq2)) 
                vdc_da_1_s = 'Diện tích hình phẳng giới hạn bởi đồ thị hàm số $y=f(x)$ với trục $Ox$ trên đoạn $[%s;%s]$ là $%s$' %(latex(x1),latex(x2),latex(kq2+1)) 
                list_vdc_da_1=[vdc_da_1_d,vdc_da_1_s]
                vdc_da_1=random.choice(list_vdc_da_1)


                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_vdc_1 = [vdc_da_1]

                # Nội dung lời giải
                loigiai_vdc_1 = ('Ta có \\\\ \n'
                        'Diện tích hình phẳng giới hạn bởi đồ thị các hàm số $y=f(x)$ với trục $Ox$ trên đoạn $[%s;%s]$ là \\\\ \n'
                        '$S=\\displaystyle\\int\\limits_{%s}^{%s} \\left|%s\\right|\\text{d}x=%s$$zz$'
                        %(latex(x1),latex(x2),
                            latex(x1),latex(x2),latex(f1),latex(kq2)
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
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac').replace('.', ',').replace('$zz$', '.')
            return content

