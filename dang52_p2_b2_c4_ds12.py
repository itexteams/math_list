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


def bt_dang52_p2_b2_c4_ds12(self):
            # Khai báo biến
            # Hàm chuyển đổi số thập phân sang định dạng có dấu phẩy
            def fmt(num):
                s = str(round(num, 4))
                return s.replace('.', ',')

            # Khai báo và random các biến xác suất
            pa = random.choice([0.1, 0.15, 0.2, 0.25, 0.3])
            p_ba_percent = random.randint(12, 25)
            p_bna_percent = random.randint(5, 11)

            p_ba = p_ba_percent / 100
            p_bna = p_bna_percent / 100

            # Tính P(B) dựa trên công thức xác suất toàn phần để đảm bảo tính chính xác của đề
            pb = pa * p_ba + (1 - pa) * p_bna
            pb_percent = pb * 100

            # Tính toán các đáp án
            p_not_b = 1 - pb
            p_not_b_given_not_a = 1 - p_bna
            p_not_a = 1 - pa
            p_not_a_given_not_b = (p_not_a * p_not_b_given_not_a) / p_not_b

            # Tính ngưỡng cho câu VD Cao
            threshold = math.floor(p_not_a_given_not_b * 10) / 10

            # Các sai số ngẫu nhiên cho phương án nhiễu
            false_offset_b = random.choice([0.002, 0.012])
            false_offset_b_given_a = random.choice([0.02, 0.05])
            false_offset_a = random.choice([0.01, 0.02])

            # Nội dung câu hỏi
            noidungcauhoi = ('Một trường đại học trao hai loại học bổng $A$ và $B$ cho sinh viên trong trường, một sinh viên có thể được nhận cả hai loại học bổng $A$ và $B$. Trong số các sinh viên được trao học bổng loại $A$ có %s\\%% số bạn được trao học bổng loại $B$ và trong số các sinh viên không được trao học bổng loại $A$ có %s\\%% số bạn được trao học bổng loại $B$. Có %s\\%% số sinh viên toàn trường được trao học bổng loại $B$. Chọn ngẫu nhiên một sinh viên trong trường.' 
                             % (fmt(p_ba_percent), fmt(p_bna_percent), fmt(pb_percent)))

            ########################################################################
            # Nhận biết ############################################
            # Các đáp án
            nb_da_1_d = '\\True Xác suất để sinh viên đó không được trao học bổng loại $B$ là $%s$' % (fmt(p_not_b))
            nb_da_1_s = 'Xác suất để sinh viên đó không được trao học bổng loại $B$ là $%s$' % (fmt(p_not_b + false_offset_b))
            list_nb_da_1=[nb_da_1_d,nb_da_1_s]
            nb_da_1=random.choice(list_nb_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_nb_1 = [nb_da_1]

            # Nội dung lời giải
            loigiai_nb_1 = ('Gọi $A$ là biến cố "Sinh viên được trao học bổng loại $A$".\\\\ Gọi $B$ là biến cố "Sinh viên được trao học bổng loại $B$".\\\\ Theo giả thiết: $P(B|A) = %s$, $P(B|\\overline{A}) = %s$, $P(B) = %s$.\\\\ Xác suất để sinh viên đó không được trao học bổng loại $B$ là $P(\\overline{B}) = 1 - P(B) = 1 - %s = %s$.' 
                            % (fmt(p_ba), fmt(p_bna), fmt(pb), fmt(pb), fmt(p_not_b)))

            # Đưa các lời giải vào danh sách lời giải
            list_nb_2 = [loigiai_nb_1]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_nb = list(zip(list_nb_1, list_nb_2))

            # Xáo trộn danh sách kết hợp
            random.shuffle(combined_nb)

            # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
            shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)

            ########################################################################
            # Thông hiểu ############################################
            # Các đáp án
            th_da_1_d = '\\True Xác suất để sinh viên đó không được trao học bổng loại $B$, biết sinh viên đó không được trao học bổng loại $A$, là $%s$' % (fmt(p_not_b_given_not_a))  
            th_da_1_s = 'Xác suất để sinh viên đó không được trao học bổng loại $B$, biết sinh viên đó không được trao học bổng loại $A$, là $%s$' % (fmt(p_not_b_given_not_a - false_offset_b_given_a))   
            list_th_da_1=[th_da_1_d,th_da_1_s]
            th_da_1=random.choice(list_th_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_th_1 = [th_da_1]

            # Nội dung lời giải
            loigiai_th_1 = ('Ta có xác suất để sinh viên không được trao học bổng loại $B$, biết sinh viên đó không được trao học bổng loại $A$ là: $P(\\overline{B}|\\overline{A}) = 1 - P(B|\\overline{A}) = 1 - %s = %s$.'        
                       % (fmt(p_bna), fmt(p_not_b_given_not_a)))

            # Đưa các lời giải vào danh sách lời giải
            list_th_2 = [loigiai_th_1]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_th = list(zip(list_th_1, list_th_2))

            # Xáo trộn danh sách kết hợp
            random.shuffle(combined_th)

            # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
            shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)

            ######################################################################## 
            # Vận dụng ############################################
            # Các đáp án
            vd_da_1_d = '\\True Xác suất để sinh viên đó không được trao học bổng loại $A$ là $%s$' % (fmt(p_not_a))  
            vd_da_1_s = 'Xác suất để sinh viên đó không được trao học bổng loại $A$ là $%s$' % (fmt(p_not_a - false_offset_a))  
            list_vd_da_1=[vd_da_1_d,vd_da_1_s]
            vd_da_1=random.choice(list_vd_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vd_1 = [vd_da_1]

            # Nội dung lời giải
            loigiai_vd_1 = ('Theo công thức xác suất toàn phần ta có:\\\\ $P(B) = P(A) \\cdot P(B|A) + P(\\overline{A}) \\cdot P(B|\\overline{A})$\\\\ $\\Leftrightarrow %s = P(A) \\cdot %s + (1 - P(A)) \\cdot %s$\\\\ $\\Leftrightarrow P(A) \\cdot (%s - %s) = %s - %s$\\\\ $\\Leftrightarrow P(A) = %s$.\\\\ Suy ra xác suất sinh viên không được trao học bổng loại $A$ là: $P(\\overline{A}) = 1 - P(A) = 1 - %s = %s$.'  
                       % (fmt(pb), fmt(p_ba), fmt(p_bna), fmt(p_ba), fmt(p_bna), fmt(pb), fmt(p_bna), fmt(pa), fmt(pa), fmt(p_not_a)))

            # Đưa các lời giải vào danh sách lời giải
            list_vd_2 = [loigiai_vd_1]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_vd = list(zip(list_vd_1, list_vd_2))

            # Xáo trộn danh sách kết hợp
            random.shuffle(combined_vd)

            # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
            shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)

            ######################################################################## 
            # Vận dụng cao ############################################
            # Các đáp án
            vdc_da_1_d = '\\True Xác suất để sinh viên đó không được trao học bổng loại $A$, biết sinh viên đó không được trao học bổng loại $B$, lớn hơn $%s$' % (fmt(threshold)) 
            vdc_da_1_s = 'Xác suất để sinh viên đó không được trao học bổng loại $A$, biết sinh viên đó không được trao học bổng loại $B$, nhỏ hơn $%s$' % (fmt(threshold)) 
            list_vdc_da_1=[vdc_da_1_d,vdc_da_1_s]
            vdc_da_1=random.choice(list_vdc_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vdc_1 = [vdc_da_1]

            # Nội dung lời giải
            loigiai_vdc_1 = ('Xác suất để sinh viên đó không được trao học bổng loại $A$, biết sinh viên đó không được trao học bổng loại $B$ là:\\\\ $P(\\overline{A}|\\overline{B}) = \\frac{P(\\overline{A}) \\cdot P(\\overline{B}|\\overline{A})}{P(\\overline{B})} = \\frac{%s \\cdot %s}{%s} \\approx %s$.\\\\ Vì $%s > %s$ nên ta có thể kết luận được tính đúng sai của mệnh đề.'
                       % (fmt(p_not_a), fmt(p_not_b_given_not_a), fmt(p_not_b), fmt(p_not_a_given_not_b), fmt(p_not_a_given_not_b), fmt(threshold)))

            # Đưa các lời giải vào danh sách lời giải
            list_vdc_2 = [loigiai_vdc_1]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_vdc = list(zip(list_vdc_1, list_vdc_2))

            # Xáo trộn danh sách kết hợp
            random.shuffle(combined_vdc)

            # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
            shuffled_answers_vdc, shuffled_solutions_vdc = zip(*combined_vdc)

            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            # Lặp đến khi đáp án có từ 1 đến 3 đúng
            while True:
                nb_da_1 = random.choice(list_nb_da_1)
                th_da_1 = random.choice(list_th_da_1)
                vd_da_1 = random.choice(list_vd_da_1)
                vdc_da_1 = random.choice(list_vdc_da_1)

                answers = [nb_da_1, th_da_1, vd_da_1, vdc_da_1]
                true_count = count_true_answers(answers)

                if 1 <= true_count <= 3:
                    break

            # Gán lại vào list
            list_nb_1 = [nb_da_1]
            list_th_1 = [th_da_1]
            list_vd_1 = [vd_da_1]
            list_vdc_1 = [vdc_da_1]

            combined_nb = list(zip(list_nb_1, list_nb_2))
            combined_th = list(zip(list_th_1, list_th_2))
            combined_vd = list(zip(list_vd_1, list_vd_2))
            combined_vdc = list(zip(list_vdc_1, list_vdc_2))

            random.shuffle(combined_nb)
            random.shuffle(combined_th)
            random.shuffle(combined_vd)
            random.shuffle(combined_vdc)

            shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)
            shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)
            shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)
            shuffled_answers_vdc, shuffled_solutions_vdc = zip(*combined_vdc)

            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+
                str(noidungcauhoi)+ '\n'
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
                '\\end{ex}\n \\end{minipage}\n\n')
            return content

