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


def bt_dang11_p2_b2_c1_ds12(self):
            # Khai báo biến
            x=symbols('x')
            k=randint(2,5)
            a=100*k
            b=randint(3,5)
            i=randint(19,22)
            gia=1000*i
            bt=a*x+b
            t=30
            t1=t/60

            kq1=a*(t1**2-t1**3)+b
            kq2=kq1-b
            kq3=kq2*gia
            # Nội dung câu hỏi
            noidungcauhoi = ('''Người ta bơm xăng vào bình xăng của một xe ô tôzz Biết rằng thể tích $V$ (tính theo lít) của lượng xăng trong bình xăng được tính theo thời gian bơm xăng $t$ (phút) được cho bởi công thức:\\\\
                            $V(t)=%s(t^2-t^3)+%s$ với $0 \\le t \\le 0,5$zz \\\\
                                Gọi $V'(t)$ là tốc độ tăng thể tích tại thời điểm $t$ với $0 \\le t \\le 0,5$zz Biết $1$ lít xăng có giá $%s$ đồngzz'''                 
                            %(latex(a),latex(b),latex(gia)
                                ))

            ######################################################################## Nhận biết ############################################
            # Các đáp án
            nb_da_1_d = '\\True Lượng xăng ban đầu trong bình là $%s$ lít'%(latex(b))
            nb_da_1_s = 'Lượng xăng ban đầu trong bình là $%s$ lít'%(latex(b+1))
            list_nb_da_1=[nb_da_1_d,nb_da_1_s]
            nb_da_1=random.choice(list_nb_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_nb_1 = [nb_da_1]

            # Nội dung lời giải
            loigiai_nb_1 = ('''Lượng xăng ban đầu trong bình là \\\\
                            $V(0)=%s (0^2-0^3)+%s=%s$ lítzz'''
                        %(latex(a),latex(b),latex(b)
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
            th_da_1_d = '\\True Sau khi bơm $%s$ giây thì bình xăng đầy. Số tiền người mua phải trả là $%s$ đồng' %(latex(t),latex(kq3))  
            th_da_1_s = 'Sau khi bơm $%s$ giây thì bình xăng đầy. Số tiền người mua phải trả là $%s$ đồng' %(latex(t),latex(kq3+1000))   
            list_th_da_1=[th_da_1_d,th_da_1_s]
            th_da_1=random.choice(list_th_da_1)


            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_th_1 = [th_da_1]

            # Nội dung lời giải
            loigiai_th_1 = ('''Ta có $%s$ giây $=%s$ phútzz \\\\
                            Suy ra $V(%s)=%s(%s^2-%s^3)+%s=%s$ lítzz \\\\
                                Khi đó số xăng đã mua là $%s-%s=%s$ lítzz \\\\
                                    Vậy số tiền người mua phải trả là $%s \\cdot %s=%s$ đồngzz'''       
                        %(latex(t),latex(t1),
                        latex(t1),latex(a),latex(t1),latex(t1),latex(b),latex(kq1),
                        latex(kq1),latex(b),latex(kq2),
                        latex(kq2),latex(gia),latex(kq3)
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
            vd_da_1_d = '\\True Khi xăng chảy vào bình xăng thì tốc độ tăng thể tích là lớn nhất vào thời điểm ở giây thứ $20$' 
            vd_da_1_s = 'Khi xăng chảy vào bình xăng thì tốc độ tăng thể tích là lớn nhất vào thời điểm ở giây thứ $21$'
            list_vd_da_1=[vd_da_1_d,vd_da_1_s]
            vd_da_1=random.choice(list_vd_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vd_1 = [vd_da_1]

            # Nội dung lời giải
            loigiai_vd_1 = ('''Xét hàm số $V'(t)=%s(2t-3t^2)$ với $0 \\le t \\le 0,5$, ta có \\\\
                            $V''(t)=%s(2-6t)$zz \\\\
                                $V''(t)=0 \\Leftrightarrow %s(2-6t)=0 \\Leftrightarrow t=\\frac{1}{3}$zz
                            Với $V'(0)=0; V'\\left(\\frac{1}{3}\\right)=%s; V'(0,5)=%s$zz \\\\
                            Suy ra $V'(t)_{max}=V'\\left(\\frac{1}{3}\\right)=%s$zz \\\\
                                Vậy tại thời điểm ở giây thứ $\\frac{1}{3} \\cdot 60=20$ giây thì tốc độ tăng thể tích là lớn nhấtzz'''
                        %(latex(a),
                        latex(a),latex(a),
                        latex(a*(2*Rational(1,3)-3*(Rational(1,3))**2)),latex(a*(2*Rational(1,2)-3*(Rational(1,2))**2)),
                        latex(a*(2*Rational(1,3)-3*(Rational(1,3))**2))
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
            vdc_da_1_d = '\\True Phương trình $V\'(t)=0$ có một nghiệm thuộc đoạn $\\left[0; \\frac{1}{2} \\right]$'
            vdc_da_1_s = 'Phương trình $V\'(t)=0$ có hai nghiệm thuộc đoạn $\\left[0; \\frac{1}{2} \\right]$'
            list_vdc_da_1=[vdc_da_1_d,vdc_da_1_s]
            vdc_da_1=random.choice(list_vdc_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vdc_1 = [vdc_da_1]

            # Nội dung lời giải
            loigiai_vdc_1 = ('''Phương trình $V'(t)=0 \\Leftrightarrow %s(2t-3t^2)=0 \\Leftrightarrow \\hoac{& t=0 \\\\& t=\\frac{2}{3} \\notin \\left[0; \\frac{1}{2} \\right]zz}$ \\\\
                            Vậy phương trình có một nghiệm thuộc đoạn $\\left[0; \\frac{1}{2} \\right]$zz'''
                        %(latex(a),

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
                '\\end{ex}\n \\end{minipage} \n\n').replace('.', ',').replace('zz', '.').replace(',0$','$')
            return content

