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


def bt_dang1_p2_b2_c3_hh10(self):
            # Khai báo biến
            x=symbols('x')
            y=symbols('y')
            a1=randint(-9,9)
            b1=randint(-9,9)

            a2=randint(-9,9)
            b2=randint(-9,9)

            a3=randint(-9,9)
            b3=randint(-9,9)

            xb=randint(-9,9)
            yb=randint(-9,9)

            xc=randint(-9,9)
            yc=randint(-9,9)
            while  a1*xb+b1*yb!=a1*xc+b1*yc or a1*b2*b3==0 or xb==xc:
                a1=randint(-9,9)
                b1=randint(-9,9)

                a2=randint(-9,9)
                b2=randint(-9,9)

                a3=randint(-9,9)
                b3=randint(-9,9)


                xb=randint(-9,9)
                yb=randint(-9,9)

                xc=randint(-9,9)
                yc=randint(-9,9)


            bc=a1*x+b1*y-a1*xb-b1*yb
            dcb=a2*x+b2*y-a2*xb-b2*yb
            dcc=a3*x+b3*y-a3*xc-b3*yc

            dtab=-b3*x+a3*y+b3*xb-a3*yb
            dtac=-b2*x+a2*y+b2*xc-a2*yc


            # Định nghĩa hệ phương trình
            eq1 = Eq(-b3*x+a3*y, -b3*xb+a3*yb)
            eq2 = Eq(-b2*x+a2*y, -b2*xc+a2*yc)

            # Giải hệ phương trình
            solution = solve((eq1, eq2), (x, y))

            # Tách riêng nghiệm
            xa = solution[x]
            ya = solution[y]



            # Nội dung câu hỏi
            noidungcauhoi = ('Cho tam giác $ABC$ có phương trình của đường thẳng $BC: %s=0$, phương trình các đường cao kẻ từ $B,C$ lần lượt là $%s=0;%s=0$.'
                            %(latex(bc),latex(dcb),latex(dcc)))



            ######################################################################## Nhận biết ############################################
            # Các đáp án
            nb_da_1_d = '\\True Điểm $B$ có tọa độ là $(%s;%s)$'%(latex(xb),latex(yb))
            nb_da_1_s = 'Điểm $B$ có tọa độ là $(%s;%s)$'%(latex(xb+1),latex(yb))
            list_nb_da_1=[nb_da_1_d,nb_da_1_s]
            nb_da_1=random.choice(list_nb_da_1)

            nb_da_2_d = '\\True Điểm $B$ có tọa độ là $(%s;%s)$'%(latex(xb),latex(yb))
            nb_da_2_s = 'Điểm $B$ có tọa độ là $(%s;%s)$'%(latex(xb),latex(yb+1))
            list_nb_da_2=[nb_da_2_d,nb_da_2_s]

            nb_da_2=random.choice(list_nb_da_2)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_nb_1 = [nb_da_1, nb_da_2]

            # Nội dung lời giải
            loigiai_nb_1 = ('Tọa độ điểm $B$ là nghiệm của hệ phương trình $\\heva{& %s=0\\\\& %s=0}\\Leftrightarrow\\heva{& x=%s\\\\& y=%s}$.\\\\ \n'
                            'Vậy tọa độ điểm $B$ là $(%s;%s)$'
                            %(latex(bc),latex(dcb),latex(xb),latex(yb),latex(xb),latex(yb),)
                        )
            loigiai_nb_2 = ('Tọa độ điểm $B$ là nghiệm của hệ phương trình $\\heva{& %s=0\\\\& %s=0}\\Leftrightarrow\\heva{& x=%s\\\\& y=%s}$.\\\\ \n'
                            'Vậy tọa độ điểm $B$ là $(%s;%s)$'
                            %(latex(bc),latex(dcb),latex(xb),latex(yb),latex(xb),latex(yb),)
                        )
            # Đưa các lời giải vào danh sách lời giải
            list_nb_2 = [loigiai_nb_1, loigiai_nb_2]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_nb = list(zip(list_nb_1, list_nb_2))

            # Xáo trộn danh sách kết hợp
            random.shuffle(combined_nb)

            # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
            shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)

            ######################################################################## Thông hiểu ############################################
            # Các đáp án
            th_da_1_d = '\\True Điểm $C$ có tọa độ là $(%s;%s)$'%(latex(xc),latex(yc))
            th_da_1_s = 'Điểm $C$ có tọa độ là $(%s;%s)$'%(latex(xc),latex(yc+1))
            list_th_da_1=[th_da_1_d,th_da_1_s]
            th_da_1=random.choice(list_th_da_1)

            th_da_2_d = '\\True Điểm $C$ có tọa độ là $(%s;%s)$'%(latex(xc),latex(yc))
            th_da_2_s = 'Điểm $C$ có tọa độ là $(%s;%s)$'%(latex(xc+1),latex(yc))
            list_th_da_2=[th_da_2_d,th_da_2_s]

            th_da_2=random.choice(list_th_da_2)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_th_1 = [th_da_1, th_da_2]

            # Nội dung lời giải
            loigiai_th_1 = ('Tọa độ điểm $C$ là nghiệm của hệ phương trình $\\heva{& %s=0\\\\& %s=0}\\Leftrightarrow\\heva{& x=%s\\\\& y=%s}$.\\\\ \n'
                            'Vậy tọa độ điểm $C$ là $(%s;%s)$'
                            %(latex(bc),latex(dcc),latex(xc),latex(yc),latex(xc),latex(yc),)
                        )
            loigiai_th_2 = ('Tọa độ điểm $C$ là nghiệm của hệ phương trình $\\heva{& %s=0\\\\& %s=0}\\Leftrightarrow\\heva{& x=%s\\\\& y=%s}$.\\\\ \n'
                            'Vậy tọa độ điểm $C$ là $(%s;%s)$'
                            %(latex(bc),latex(dcc),latex(xc),latex(yc),latex(xc),latex(yc),)
                        )

            # Đưa các lời giải vào danh sách lời giải
            list_th_2 = [loigiai_th_1, loigiai_th_2]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_th = list(zip(list_th_1, list_th_2))

            # Xáo trộn danh sách kết hợp
            random.shuffle(combined_th)

            # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
            shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)

            ######################################################################## Vận dụng ############################################
            # Các đáp án
            vd_da_1_d = '\\True Phương trình đường thẳng $AB$ là $%s=0$'%(latex(dtab))
            vd_da_1_s = 'Phương trình đường thẳng $AB$ là $ %s=0$'%(latex(dtab+1))
            list_vd_da_1=[vd_da_1_d,vd_da_1_s]
            vd_da_1=random.choice(list_vd_da_1)

            vd_da_2_d = '\\True Phương trình đường thẳng $AC$ là $%s=0$'%(latex(dtac))
            vd_da_2_s = 'Phương trình đường thẳng $AC$ là $%s=0$'%(latex(dtac-1))
            list_vd_da_2=[vd_da_2_d,vd_da_2_s]

            vd_da_2=random.choice(list_vd_da_2)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vd_1 = [vd_da_1, vd_da_2]

            # Nội dung lời giải
            loigiai_vd_1 = ('Đường thẳng $AB$ đi qua $B(%s;%s)$ và nhận vectơ chỉ phương $u_1(%s;%s)$ của đường cao kẻ từ $C$ làm vectơ pháp tuyến có phương trình là '
                            '$$%s(x-%s)+%s(y-%s)=0 \\Leftrightarrow %s=0.$$'

                            %(latex(xb),latex(yb),latex(-b3),latex(a3),latex(-b3),latex(xb),latex(a3),latex(yb),latex(dtab),)

                        )
            loigiai_vd_2 = ('Đường thẳng $AC$ đi qua $C(%s;%s)$ và nhận vectơ chỉ phương $u_2(%s;%s)$ của đường cao kẻ từ $B$ làm vectơ pháp tuyến có phương trình là '
                            '$$%s(x-%s)+%s(y-%s)=0 \\Leftrightarrow %s=0.$$'

                            %(latex(xc),latex(yc),latex(-b2),latex(a2),latex(-b2),latex(xc),latex(a2),latex(yc),latex(dtac),
                            )
                        )

            # Đưa các lời giải vào danh sách lời giải
            list_vd_2 = [loigiai_vd_1, loigiai_vd_2]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_vd = list(zip(list_vd_1, list_vd_2))

            # Xáo trộn danh sách kết hợp
            random.shuffle(combined_vd)

            # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
            shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)

            ######################################################################## Vận dụng cao ############################################
            # Các đáp án
            vdc_da_1_d = '\\True Điểm $A$ có tọa độ $\\left(%s;%s\\right)$'%(latex(xa),latex(ya))
            vdc_da_1_s = 'Điểm $A$ có tọa độ $\\left(%s;%s\\right)$'%(latex(xa+1),latex(ya))
            list_vdc_da_1=[vdc_da_1_d,vdc_da_1_s]
            vdc_da_1=random.choice(list_vdc_da_1)

            vdc_da_2_d = '\\True Điểm $A$ có tọa độ $\\left(%s;%s\\right)$'%(latex(xa),latex(ya))
            vdc_da_2_s = 'Điểm $A$ có tọa độ $\\left(%s;%s\\right)$'%(latex(xa),latex(ya-1))
            list_vdc_da_2=[vdc_da_2_d,vdc_da_2_s]

            vdc_da_2=random.choice(list_vdc_da_2)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vdc_1 = [vdc_da_1, vdc_da_2]

            # Nội dung lời giải
            loigiai_vdc_1 = ('Đường thẳng $AB$ đi qua $B(%s;%s)$ và nhận vectơ chỉ phương $u_1(%s;%s)$ của đường cao kẻ từ $C$ làm vectơ pháp tuyến có phương trình là '
                            '$%s(x-%s)+%s(y-%s)=0 \\Leftrightarrow %s=0$.\\\\ \n'
                            'Đường thẳng $AC$ đi qua $C(%s;%s)$ và nhận vectơ chỉ phương $u_2(%s;%s)$ của đường cao kẻ từ $B$ làm vectơ pháp tuyến có phương trình là '
                            '$%s(x-%s)+%s(y-%s)=0 \\Leftrightarrow %s=0$.\\\\ \n'
                            'Tọa độ điểm $A$ là nghiệm của hệ phương trình $\\heva{& %s=0\\\\& %s=0}\\Leftrightarrow\\heva{& x=%s\\\\& y=%s}$.\\\\ \n'
                            'Vậy tọa độ điểm $A$ là $\\left(%s;%s\\right)$'
                            %(latex(xb),latex(yb),latex(-b3),latex(a3),latex(-b3),latex(xb),latex(a3),latex(yb),latex(dtab),
                            latex(xc),latex(yc),latex(-b2),latex(a2),latex(-b2),latex(xc),latex(a2),latex(yc),latex(dtac),
                            latex(dtab),latex(dtac),latex(xa),latex(ya),latex(xa),latex(ya),)
                        )
            loigiai_vdc_2 = ('Đường thẳng $AB$ đi qua $B(%s;%s)$ và nhận vectơ chỉ phương $u_1(%s;%s)$ của đường cao kẻ từ $C$ làm vectơ pháp tuyến có phương trình là '
                            '$%s(x-%s)+%s(y-%s)=0 \\Leftrightarrow %s=0$.\\\\ \n'
                            'Đường thẳng $AC$ đi qua $C(%s;%s)$ và nhận vectơ chỉ phương $u_2(%s;%s)$ của đường cao kẻ từ $B$ làm vectơ pháp tuyến có phương trình là '
                            '$%s(x-%s)+%s(y-%s)=0 \\Leftrightarrow %s=0$.\\\\ \n'
                            'Tọa độ điểm $A$ là nghiệm của hệ phương trình $\\heva{& %s=0\\\\& %s=0}\\Leftrightarrow\\heva{& x=%s\\\\& y=%s}$.\\\\ \n'
                            'Vậy tọa độ điểm $A$ là $\\left(%s;%s\\right)$'
                            %(latex(xb),latex(yb),latex(-b3),latex(a3),latex(-b3),latex(xb),latex(a3),latex(yb),latex(dtab),
                            latex(xc),latex(yc),latex(-b2),latex(a2),latex(-b2),latex(xc),latex(a2),latex(yc),latex(dtac),
                            latex(dtab),latex(dtac),latex(xa),latex(ya),latex(xa),latex(ya),)
                        )

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
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac','\\dfrac').replace('++','+').replace('--','+').replace('+-','-').replace('-+','-')
            return content

