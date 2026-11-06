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


def bt_dang1_p2_b2_c3_ds10(self):
            # Khai báo biến
            lisdang=['1','2']
            dang=random.choice(lisdang)

            if dang=='2':
                # Khai báo biến
                x1=randint(1,50)
                x2=randint(1,50)
                x3=randint(1,50)
                x4=randint(1,50)
                x5=randint(1,50)
                x6=randint(1,50)
                x7=randint(1,50)
                x8=randint(1,50)
                x9=randint(1,50)
                x10=randint(1,50)
                x11=randint(1,50)
                x12=randint(1,50)
                x13=randint(1,50)

                n=13

                xtb = Decimal(float((x1+x2+x3+x4+x5+x6+x7+x8+x9+x10+x11+x12+x13)/n)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
                xtbs = Decimal(float((x1+x2+x3+x4+x5+x6+x7+x8+x9+x10+x11+x12+x13)/n+1)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)

                # Đưa các số vào danh sách
                numbers = [x1, x2, x3, x4, x5, x6, x7, x8, x9, x10,x11,x12,x13]

                # Sắp xếp danh sách theo thứ tự tăng dần
                numbers.sort()

                # Tìm hai số đứng giữa
                x_7 = numbers[6]
                me=x_7

                x_3 = numbers[2]
                x_4 = numbers[3]
                q1=(x_3 +x_4)/2

                x_10 = numbers[9]
                x_11 = numbers[10]
                q3=(x_10+x_11)/2 

                # Nội dung câu hỏi
                noidungcauhoi = ('Cho mẫu số liệu \n'
                                '$$%s\\hspace*{0.5cm} %s\\hspace*{0.5cm} %s\\hspace*{0.5cm} %s\\hspace*{0.5cm} %s\\hspace*{0.5cm} %s\\hspace*{0.5cm} %s\\hspace*{0.5cm} %s\\hspace*{0.5cm} %s\\hspace*{0.5cm} %s\\hspace*{0.5cm} %s\\hspace*{0.5cm} %s\\hspace*{0.5cm} %s$$'

                                %(latex(x1),latex(x2),latex(x3),latex(x4),latex(x5),latex(x6),latex(x7),latex(x8),latex(x9),latex(x10),latex(x11),latex(x12),latex(x13)
                                ))

                ######################################################################## Nhận biết ############################################
                # Các đáp án
                nb_da_1_d = '\\True Tổng số các giá trị là $%s$' %(latex(n))
                nb_da_1_s = 'Tổng số các giá trị là $%s$' %(latex(n+1))
                list_nb_da_1=[nb_da_1_d,nb_da_1_s]
                nb_da_1=random.choice(list_nb_da_1)

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_nb_1 = [nb_da_1]

                # Nội dung lời giải
                loigiai_nb_1 = ('Tổng số các giá trị là $%s$$zz$' %(latex(n))
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
                th_da_1_d = '\\True Số trung bình của dãy số liệu là $\\bar{x}=%s$' %(latex(xtb))
                th_da_1_s = 'Số trung bình của dãy số liệu là $\\bar{x}=%s$' %(latex(xtbs))
                list_th_da_1=[th_da_1_d,th_da_1_s]
                th_da_1=random.choice(list_th_da_1)


                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_th_1 = [th_da_1]

                # Nội dung lời giải
                loigiai_th_1 = ('Số trung bình của mẫu số liệu là \\\\ \n'
                        '\\hspace*{1cm} $\\bar{x}=\\dfrac{%s+%s+%s+%s+%s+%s+%s+%s+%s+%s+%s+%s+%s}{13}=%s$$zz$'
                        %(latex(x1),latex(x2),latex(x3),latex(x4),latex(x5),latex(x6),latex(x7),latex(x8),latex(x9),latex(x10),latex(x11),latex(x12),latex(x13),
                        latex(xtb)
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
                vd_da_1_d = '\\True Trung vị của dãy số liệu là $M_e=%s$' %(latex(me))
                vd_da_1_s = 'Trung vị của dãy số liệu là $M_e=%s$' %(latex(me+1))
                list_vd_da_1=[vd_da_1_d,vd_da_1_s]
                vd_da_1=random.choice(list_vd_da_1)

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_vd_1 = [vd_da_1]

                # Nội dung lời giải
                loigiai_vd_1 = ('Xắp xếp dãy số theo thứ tự tăng dần ta được \\\\ \n'
                        '$$%s$$ \n'
                        'Tổng của mẫu số liệu là $n=%s$ nên \\\\ \n'
                        '\\hspace*{1cm} Trung vị của mẫu số liệu là $M_e=x_7=%s$$zz$'
                        %(latex(numbers),latex(n),
                        latex(me),         
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
                vdc_da_1_d = '\\True Tứ phân vị thứ nhất của mẫu số liệu là $Q_1=%s$' %(latex(q1))
                vdc_da_1_s = 'Tứ phân vị thứ nhất của mẫu số liệu là $Q_1=%s$' %(latex(q1+1))
                list_vdc_da_1=[vdc_da_1_d,vdc_da_1_s]
                vdc_da_1=random.choice(list_vdc_da_1)

                vdc_da_2_d = '\\True Tứ phân vị thứ ba của mẫu số liệu là $Q_3=%s$' %(latex(q3))
                vdc_da_2_s = 'Tứ phân vị thứ ba của mẫu số liệu là $Q_3=%s$' %(latex(q3))
                list_vdc_da_2=[vdc_da_2_d,vdc_da_2_s]

                vdc_da_2=random.choice(list_vdc_da_2)

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_vdc_1 = [vdc_da_1, vdc_da_2]

                # Nội dung lời giải
                loigiai_vdc_1 = ('Xắp xếp dãy số theo thứ tự tăng dần ta được \\\\ \n'
                        '$$%s$$ \n'
                        'Tổng của mẫu số liệu là $n=%s$ nên \\\\ \n'
                        '\\hspace*{1cm} Trung vị của mẫu số liệu là $M_e=x_7=%s$$zz$ \\\\ \n'
                        '\\hspace*{1cm} Tứ phân vị thứ nhất của mẫu số liệu là $Q_1=\\dfrac{x_3+x_4}{2}=\\dfrac{%s+%s}{2}=%s$$zz$'
                        %(latex(numbers),latex(n),
                        latex(me),
                        latex(x_3),latex(x_4),latex(q1)

                        ))
                loigiai_vdc_2 = ('Xắp xếp dãy số theo thứ tự tăng dần ta được \\\\ \n'
                        '$$%s$$ \n'
                        'Tổng của mẫu số liệu là $n=%s$ nên \\\\ \n'
                        '\\hspace*{1cm} Trung vị của mẫu số liệu là $M_e=x_7=%s$$zz$ \\\\ \n'
                        '\\hspace*{1cm} Tứ phân vị thứ nhất của mẫu số liệu là $Q_1=\\dfrac{x_3+x_4}{2}=\\dfrac{%s+%s}{2}=%s$$zz$'
                        '\\hspace*{1cm} Tứ phân vị thứ ba của mẫu số liệu là $Q_3=\\dfrac{x_10+x_11}{2}=\\dfrac{%s+%s}{2}=%s$$zz$'
                        %(latex(numbers),latex(n),
                        latex(me),
                        latex(x_3),latex(x_4),latex(q1),
                        latex(x_10),latex(x_11),latex(q3)

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
                # Khai báo biến
                x1=randint(1,20)
                x2=randint(1,20)
                x3=randint(1,20)
                x4=randint(1,20)
                x5=randint(1,20)
                x6=randint(1,20)
                x7=randint(1,20)
                x8=randint(1,20)
                x9=randint(1,20)
                x10=randint(1,20)

                n=10

                xtb = Decimal(float((x1+x2+x3+x4+x5+x6+x7+x8+x9+x10)/n)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
                xtbs = Decimal(float((x1+x2+x3+x4+x5+x6+x7+x8+x9+x10)/n+1)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)

                # Đưa các số vào danh sách
                numbers = [x1, x2, x3, x4, x5, x6, x7, x8, x9, x10]

                # Sắp xếp danh sách theo thứ tự tăng dần
                numbers.sort()

                # Tìm hai số đứng giữa
                x_5 = numbers[4]
                x_6 = numbers[5]
                me=(x_5+x_6)/2

                x_3 = numbers[2]
                q1=x_3 

                x_8 = numbers[7]
                q3=x_8  

                # Nội dung câu hỏi
                noidungcauhoi = ('Cho mẫu số liệu \n'
                                '$$%s\\hspace*{0.5cm} %s\\hspace*{0.5cm} %s\\hspace*{0.5cm} %s\\hspace*{0.5cm} %s\\hspace*{0.5cm} %s\\hspace*{0.5cm} %s\\hspace*{0.5cm} %s\\hspace*{0.5cm} %s\\hspace*{0.5cm} %s$$'

                                %(latex(x1),latex(x2),latex(x3),latex(x4),latex(x5),latex(x6),latex(x7),latex(x8),latex(x9),latex(x10)
                                ))

                ######################################################################## Nhận biết ############################################
                # Các đáp án
                nb_da_1_d = '\\True Tổng số các giá trị là $%s$' %(latex(n))
                nb_da_1_s = 'Tổng số các giá trị là $%s$' %(latex(n+1))
                list_nb_da_1=[nb_da_1_d,nb_da_1_s]
                nb_da_1=random.choice(list_nb_da_1)

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_nb_1 = [nb_da_1]

                # Nội dung lời giải
                loigiai_nb_1 = ('Tổng số các giá trị là $%s$$zz$' %(latex(n))
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
                th_da_1_d = '\\True Số trung bình của dãy số liệu là $\\bar{x}=%s$' %(latex(xtb))
                th_da_1_s = 'Số trung bình của dãy số liệu là $\\bar{x}=%s$' %(latex(xtbs))
                list_th_da_1=[th_da_1_d,th_da_1_s]
                th_da_1=random.choice(list_th_da_1)


                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_th_1 = [th_da_1]

                # Nội dung lời giải
                loigiai_th_1 = ('Số trung bình của mẫu số liệu là \\\\ \n'
                        '\\hspace*{1cm} $\\bar{x}=\\dfrac{%s+%s+%s+%s+%s+%s+%s+%s+%s+%s}{10}=%s$$zz$'
                        %(latex(x1),latex(x2),latex(x3),latex(x4),latex(x5),latex(x6),latex(x7),latex(x8),latex(x9),latex(x10),
                        latex(xtb)
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
                vd_da_1_d = '\\True Trung vị của dãy số liệu là $M_e=%s$' %(latex(me))
                vd_da_1_s = 'Trung vị của dãy số liệu là $M_e=%s$' %(latex(me+1))
                list_vd_da_1=[vd_da_1_d,vd_da_1_s]
                vd_da_1=random.choice(list_vd_da_1)

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_vd_1 = [vd_da_1]

                # Nội dung lời giải
                loigiai_vd_1 = ('Xắp xếp dãy số theo thứ tự tăng dần ta được \\\\ \n'
                        '$$%s$$ \n'
                        'Tổng của mẫu số liệu là $n=10$ nên \\\\ \n'
                        '\\hspace*{1cm} Trung vị của mẫu số liệu là $M_e=\\dfrac{x_5+x_6}{2}=\\dfrac{%s+%s}{2}=%s$$zz$'
                        %(latex(numbers),
                        latex(x_5),latex(x_6),latex(me),         
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
                vdc_da_1_d = '\\True Tứ phân vị thứ nhất của mẫu số liệu là $Q_1=%s$' %(latex(q1))
                vdc_da_1_s = 'Tứ phân vị thứ nhất của mẫu số liệu là $Q_1=%s$' %(latex(q1+1))
                list_vdc_da_1=[vdc_da_1_d,vdc_da_1_s]
                vdc_da_1=random.choice(list_vdc_da_1)

                vdc_da_2_d = '\\True Tứ phân vị thứ ba của mẫu số liệu là $Q_3=%s$' %(latex(q3))
                vdc_da_2_s = 'Tứ phân vị thứ ba của mẫu số liệu là $Q_3=%s$' %(latex(q3))
                list_vdc_da_2=[vdc_da_2_d,vdc_da_2_s]

                vdc_da_2=random.choice(list_vdc_da_2)

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_vdc_1 = [vdc_da_1, vdc_da_2]

                # Nội dung lời giải
                loigiai_vdc_1 = ('Xắp xếp dãy số theo thứ tự tăng dần ta được \\\\ \n'
                        '$$%s$$ \n'
                        'Tổng của mẫu số liệu là $n=10$ nên \\\\ \n'
                        '\\hspace*{1cm} Trung vị của mẫu số liệu là $M_e=\\dfrac{x_5+x_6}{2}=\\dfrac{%s+%s}{2}=%s$$zz$ \\\\ \n'
                        '\\hspace*{1cm} Tứ phân vị thứ nhất của mẫu số liệu là $Q_1=x_3=%s$$zz$'
                        %(latex(numbers),
                        latex(x_5),latex(x_6),latex(me),
                        latex(q1)

                        ))
                loigiai_vdc_2 = ('Xắp xếp dãy số theo thứ tự tăng dần ta được \\\\ \n'
                        '$$%s$$ \n'
                        'Tổng của mẫu số liệu là $n=10$ nên \\\\ \n'
                        '\\hspace*{1cm} Trung vị của mẫu số liệu là $M_e=\\dfrac{x_5+x_6}{2}=\\dfrac{%s+%s}{2}=%s$$zz$ \\\\ \n'
                        '\\hspace*{1cm} Tứ phân vị thứ nhất của mẫu số liệu là $Q_1=x_3=%s$$zz$ \\\\ \n'
                        '\\hspace*{1cm} Tứ phân vị thứ nhất của mẫu số liệu là $Q_3=x_8=%s$$zz$'
                        %(latex(numbers),
                        latex(x_5),latex(x_6),latex(me),
                        latex(q1),latex(q3)

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
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac').replace('.', ',').replace('$zz$', '.').replace('\\left[', '').replace('\\right]', '').replace(',0$', '$').replace(', \\', '\\hspace*{0.5cm}')
            return content

