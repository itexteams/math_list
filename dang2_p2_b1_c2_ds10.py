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


def bt_dang2_p2_b1_c2_ds10(self):
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)
            if dang=='1':
                # Khai báo biến
                x = symbols('x')
                y = symbols('y')

                a=randint(1,5)
                b=randint(1,5)
                t=randint(15,30)

                x0=randint(1,5)
                y0=randint(1,5)

                x1=randint(3,7)
                y1=randint(2,9)

                x2=randint(1,5)
                y2=randint(1,5)

                x3=randint(3,7)
                y3=randint(2,9)

                while a==b or a*x0+b*y0>t or a*x1+b*y1<=t or a*x2+b*y2>t or a*x3+b*y3<=t:
                    a=randint(1,5)
                    b=randint(1,5)
                    t=randint(15,30)

                    x0=randint(1,5)
                    y0=randint(1,5)

                    x1=randint(3,7)
                    y1=randint(2,9)

                    x2=randint(1,5)
                    y2=randint(1,5)

                    x3=randint(3,7)
                    y3=randint(2,9)
                bptb=a*x+b*y<=t
                xb=simplify(bptb)

            # Tìm ước chung lớn nhất (GCD) của các hệ số
                gcd = math.gcd(math.gcd(a,b),t)
            # Rút gọn các hệ số
                hs_a1 =a // gcd
                hs_b1 =b // gcd
                hs_c1 =t // gcd
            #\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
                xc = hs_a1*x+hs_b1*y<=hs_c1

                bptb1=a*x+b*y<t
                xbs1=simplify(bptb1)
                bptb2=a*x+b*y>=t
                xbs2=simplify(bptb2)


                # Nội dung câu hỏi
                noidungcauhoi = ('Một đội sản xuất cần $%s$ giờ để làm xong sản phẩm loại $I$ và $%s$ giờ để làm xong sản phẩm loại $II$. '
                                'Biết thời gian tối đa cho việc sản xuất hai sản phẩm trên là $%s$ giờ. Gọi $x,y$ $(x\\in\\mathbb{N};y\\in \\mathbb{N})$ lần lượt là số sản phẩm loại $I$, loại $II$ mà đội làm được trong thời gian cho phép.'
                                %(latex(a),latex(b),latex(t),))



                ######################################################################## Nhận biết ############################################
                # Các đáp án
                nb_da_1_d = '\\True Tổng thời gian làm xong sản phẩm loại $I$ là $%s x$ giờ, tổng thời gian làm xong sản phẩm loại $II$ là $%s y$ giờ'%(latex(a),latex(b))
                nb_da_1_s = 'Tổng thời gian làm xong sản phẩm loại $I$ là $%s x$ giờ, tổng thời gian làm xong sản phẩm loại $II$ là $%s y$ giờ'%(latex(b),latex(a))
                list_nb_da_1=[nb_da_1_d,nb_da_1_s]
                nb_da_1=random.choice(list_nb_da_1)

                nb_da_2_d = '\\True Tổng thời gian làm xong sản phẩm loại $I$ là $%s x$ giờ, tổng thời gian làm xong sản phẩm loại $II$ là $%s y$ giờ'%(latex(a),latex(b))
                nb_da_2_s = 'Tổng thời gian làm xong sản phẩm loại $I$ là $%s x$ giờ, tổng thời gian làm xong sản phẩm loại $II$ là $%s y$ giờ'%(latex(b),latex(a))
                list_nb_da_2=[nb_da_2_d,nb_da_2_s]

                nb_da_2=random.choice(list_nb_da_2)

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_nb_1 = [nb_da_1, nb_da_2]

                # Nội dung lời giải
                loigiai_nb_1 = ('Tổng thời gian làm xong sản phẩm loại $I$ là $%s x$ giờ, tổng thời gian làm xong sản phẩm loại $II$ là $%s y$ giờ.'
                                %(latex(a),latex(b),
                                ))
                loigiai_nb_2 = ('Tổng thời gian làm xong sản phẩm loại $I$ là $%s x$ giờ, tổng thời gian làm xong sản phẩm loại $II$ là $%s y$ giờ.'
                                %(latex(a),latex(b),
                                ))
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
                th_da_1_d = '\\True Bất phương trình hai ẩn $x,y$ là $%s$'%(latex(xb))
                th_da_1_s = 'Bất phương trình hai ẩn $x,y$ là $%s$'%(latex(xbs1))
                list_th_da_1=[th_da_1_d,th_da_1_s]
                th_da_1=random.choice(list_th_da_1)

                th_da_2_d = '\\True Bất phương trình hai ẩn $x,y$ là $%s$'%(latex(xb))
                th_da_2_s = 'Bất phương trình hai ẩn $x,y$ là $%s$'%(latex(xbs2))
                list_th_da_2=[th_da_2_d,th_da_2_s]

                th_da_2=random.choice(list_th_da_2)

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_th_1 = [th_da_1, th_da_2]

                # Nội dung lời giải
                loigiai_th_1 = ('Ta có bất phương trình theo hai ẩn $x,y$ là $%s \\cdot x+ %s\\cdot y\\le %s \\Leftrightarrow %s$. '
                                %(latex(a),latex(b),latex(t),latex(xb),
                                ))
                loigiai_th_2 = ('Ta có bất phương trình theo hai ẩn $x,y$ là $%s \\cdot x+ %s\\cdot y\\le %s \\Leftrightarrow %s$. '
                                %(latex(a),latex(b),latex(t),latex(xb),
                                ))
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
                vd_da_1_d = '\\True $(%s;%s)$ là một nghiệm của bất phương trình theo $x,y$'%(latex(x0),latex(y0),)
                vd_da_1_s = '$(%s;%s)$ là một nghiệm của bất phương trình theo $x,y$'%(latex(x1),latex(y1),)
                list_vd_da_1=[vd_da_1_d,vd_da_1_s]
                vd_da_1=random.choice(list_vd_da_1)

                vd_da_2_d = '\\True $(%s;%s)$ là một nghiệm của bất phương trình theo $x,y$'%(latex(x0),latex(y0),)
                vd_da_2_s = '$(%s;%s)$ là một nghiệm của bất phương trình theo $x,y$'%(latex(x1),latex(y1),)
                list_vd_da_2=[vd_da_2_d,vd_da_2_s]

                vd_da_2=random.choice(list_vd_da_2)

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_vd_1 = [vd_da_1, vd_da_2]

                # Nội dung lời giải
                loigiai_vd_1 = ('Ta có $%s\\cdot %s + %s \\cdot %s =%s \\le %s$ nên cặp số $(%s;%s)$ thỏa mãn bất phương trình bậc nhất hai ẩn đã cho.\\\\ \n'
                                ' $%s\\cdot %s + %s \\cdot %s =%s > %s$ nên cặp số $(%s;%s)$ không thỏa mãn bất phương trình bậc nhất hai ẩn đã cho.'
                                %(latex(hs_a1),latex(x0),latex(hs_b1),latex(y0),latex(hs_a1*x0+hs_b1*y0),latex(hs_c1),latex(x0),latex(y0),
                                latex(hs_a1),latex(x1),latex(hs_b1),latex(y1),latex(hs_a1*x1+hs_b1*y1),latex(hs_c1),latex(x1),latex(y1),
                                ))
                loigiai_vd_2 = ('Ta có $%s\\cdot %s + %s \\cdot %s =%s \\le %s$ nên cặp số $(%s;%s)$ thỏa mãn bất phương trình bậc nhất hai ẩn đã cho.\\\\ \n'
                                ' $%s\\cdot %s + %s \\cdot %s =%s > %s$ nên cặp số $(%s;%s)$ không thỏa mãn bất phương trình bậc nhất hai ẩn đã cho.'
                                %(latex(hs_a1),latex(x0),latex(hs_b1),latex(y0),latex(hs_a1*x0+hs_b1*y0),latex(hs_c1),latex(x0),latex(y0),
                                latex(hs_a1),latex(x1),latex(hs_b1),latex(y1),latex(hs_a1*x1+hs_b1*y1),latex(hs_c1),latex(x1),latex(y1),
                                ))

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
                vdc_da_1_d = '\\True Đội sản xuất $%s$ sản phẩm loại $I$ và $%s$ sản phẩm loại $II$ đảm bảo thời gian cho phép'%(latex(x2),latex(y2))
                vdc_da_1_s = 'Đội sản xuất $%s$ sản phẩm loại $I$ và $%s$ sản phẩm loại $II$ đảm bảo thời gian cho phép'%(latex(x3),latex(y3))
                list_vdc_da_1=[vdc_da_1_d,vdc_da_1_s]
                vdc_da_1=random.choice(list_vdc_da_1)

                vdc_da_2_d = '\\True Đội sản xuất $%s$ sản phẩm loại $I$ và $%s$ sản phẩm loại $II$ không đảm bảo thời gian cho phép'%(latex(x3),latex(y3))
                vdc_da_2_s = 'Đội sản xuất $%s$ sản phẩm loại $I$ và $%s$ sản phẩm loại $II$ không đảm bảo thời gian cho phép'%(latex(x2),latex(y2))
                list_vdc_da_2=[vdc_da_2_d,vdc_da_2_s]

                vdc_da_2=random.choice(list_vdc_da_2)

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_vdc_1 = [vdc_da_1, vdc_da_2]

                # Nội dung lời giải
                loigiai_vdc_1 =('Ta có $%s\\cdot %s + %s \\cdot %s =%s \\le %s$ nên đội có thể sản xuất $%s$ sản phẩm loại $I$ và $%s$ sản phẩm loại $II$ đảm bảo thời gian cho phép.\\\\ \n'
                                'Ta có $%s\\cdot %s + %s \\cdot %s =%s > %s$ nên đội có thể sản xuất $%s$ sản phẩm loại $I$ và $%s$ sản phẩm loại $II$ không đảm bảo thời gian cho phép.'
                                %(latex(hs_a1),latex(x2),latex(hs_b1),latex(y2),latex(hs_a1*x2+hs_b1*y2),latex(hs_c1),latex(x2),latex(y2),
                                latex(hs_a1),latex(x3),latex(hs_b1),latex(y3),latex(hs_a1*x3+hs_b1*y3),latex(hs_c1),latex(x3),latex(y3),
                                ))
                loigiai_vdc_2 =('Ta có $%s\\cdot %s + %s \\cdot %s =%s \\le %s$ nên đội có thể sản xuất $%s$ sản phẩm loại $I$ và $%s$ sản phẩm loại $II$ đảm bảo thời gian cho phép.\\\\ \n'
                                'Ta có $%s\\cdot %s + %s \\cdot %s =%s > %s$ nên đội có thể sản xuất $%s$ sản phẩm loại $I$ và $%s$ sản phẩm loại $II$ không đảm bảo thời gian cho phép.'
                                %(latex(hs_a1),latex(x2),latex(hs_b1),latex(y2),latex(hs_a1*x2+hs_b1*y2),latex(hs_c1),latex(x2),latex(y2),
                                latex(hs_a1),latex(x3),latex(hs_b1),latex(y3),latex(hs_a1*x3+hs_b1*y3),latex(hs_c1),latex(x3),latex(y3),
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
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac')
            return content

