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


def bt_dang46_p2_b2_c4_ds12(self):
            # Khai báo biến
            # Hàm bổ trợ định dạng số thập phân kiểu Việt Nam (dùng dấu phẩy)
            def to_vn(val, ndigits=3):
                f_val = round(float(val), ndigits)
                if f_val.is_integer():
                    return str(int(f_val))
                s = f"{f_val:.{ndigits}f}".rstrip('0').rstrip('.')
                return s.replace('.', ',')

            # Hàm bổ trợ chuyển phân số sang định dạng LaTeX
            def to_frac_tex(frac_obj):
                if frac_obj.denominator == 1:
                    return str(frac_obj.numerator)
                return "\\frac{%s}{%s}" % (frac_obj.numerator, frac_obj.denominator)

            # Chọn ngẫu nhiên một bộ số liệu bài toán
            case = random.choice([1, 2, 3])

            if case == 1:
                pK, pS = Fraction(6, 10), Fraction(4, 10)
                pBK, pVK = Fraction(8, 10), Fraction(3, 10)
                pBS, pVS = Fraction(1, 10), Fraction(7, 10)
                thresh_a, thresh_b, thresh_c = Fraction(4, 10), Fraction(5, 10), Fraction(5, 10)
            elif case == 2:
                pK, pS = Fraction(7, 10), Fraction(3, 10)
                pBK, pVK = Fraction(7, 10), Fraction(4, 10)
                pBS, pVS = Fraction(2, 10), Fraction(6, 10)
                thresh_a, thresh_b, thresh_c = Fraction(5, 10), Fraction(5, 10), Fraction(6, 10)
            else:
                pK, pS = Fraction(5, 10), Fraction(5, 10)
                pBK, pVK = Fraction(7, 10), Fraction(3, 10)
                pBS, pVS = Fraction(3, 10), Fraction(5, 10)
                thresh_a, thresh_b, thresh_c = Fraction(4, 10), Fraction(5, 10), Fraction(5, 10)

            # Tính toán các giá trị xác suất trung gian
            pB = pBK * pK + pBS * pS
            pV = pVK * pK + pVS * pS

            pNotB = 1 - pB
            pNotBS = 1 - pBS
            pS_NotB = (pNotBS * pS) / pNotB

            pL = Fraction(1, 2) * pB + Fraction(1, 2) * pV
            pLK = Fraction(1, 2) * pBK + Fraction(1, 2) * pVK
            pK_L = (pLK * pK) / pL

            pCK = pBK * pVK
            pCS = pBS * pVS
            pK_C = (pCK * pK) / (pCK * pK + pCS * pS)

            # Nội dung câu hỏi
            noidungcauhoi = ('''Người ta nhận thấy rằng xác suất để kinh tế thế giới phát triển là %s\\%% . Trong trường hợp này, xác suất sinh lời khi đầu tư vào bất động sản là %s\\%% và đầu tư vào vàng là %s\\%% . Xác suất để kinh tế thế giới suy thoái là %s\\%% . Khi đó, xác suất sinh lời khi đầu tư vào bất động sản là %s\\%% và đầu tư vào việc mua vàng là %s\\%%.''' 
                             % (to_vn(pK*100), to_vn(pBK*100), to_vn(pVK*100), to_vn(pS*100), to_vn(pBS*100), to_vn(pVS*100)))

            ######################################################################## Nhận biết ############################################
            # Thiết lập mệnh đề đúng / sai cho khẳng định a
            is_a_vượt = pS_NotB > thresh_a
            if is_a_vượt:
                nb_da_1_d = '\\True Nếu biết một người đầu tư bất động sản không sinh lời thì xác suất kinh tế suy thoái vượt quá %s' % to_vn(thresh_a)
                nb_da_1_s = 'Nếu biết một người đầu tư bất động sản không sinh lời thì xác suất kinh tế suy thoái nhỏ hơn %s' % to_vn(thresh_a)
            else:
                nb_da_1_d = '\\True Nếu biết một người đầu tư bất động sản không sinh lời thì xác suất kinh tế suy thoái nhỏ hơn %s' % to_vn(thresh_a)
                nb_da_1_s = 'Nếu biết một người đầu tư bất động sản không sinh lời thì xác suất kinh tế suy thoái vượt quá %s' % to_vn(thresh_a)

            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]

            ######################################################################## Thông hiểu ############################################
            # Thiết lập mệnh đề đúng / sai cho khẳng định b
            is_b_lớn = pL > thresh_b
            if is_b_lớn:
                th_da_1_d = '\\True Một nhà đầu tư chọn ngẫu nhiên một trong hai hình thức là bất động sản hoặc vàng thì xác suất để sinh lời trong trường hợp này lớn hơn %s' % to_vn(thresh_b)
                th_da_1_s = 'Một nhà đầu tư chọn ngẫu nhiên một trong hai hình thức là bất động sản hoặc vàng thì xác suất để sinh lời trong trường hợp này nhỏ hơn %s' % to_vn(thresh_b)
            else:
                th_da_1_d = '\\True Một nhà đầu tư chọn ngẫu nhiên một trong hai hình thức là bất động sản hoặc vàng thì xác suất để sinh lời trong trường hợp này nhỏ hơn %s' % to_vn(thresh_b)
                th_da_1_s = 'Một nhà đầu tư chọn ngẫu nhiên một trong hai hình thức là bất động sản hoặc vàng thì xác suất để sinh lời trong trường hợp này lớn hơn %s' % to_vn(thresh_b)

            list_th_da_1 = [th_da_1_d, th_da_1_s]

            ######################################################################## Vận dụng ############################################
            # Thiết lập mệnh đề đúng / sai cho khẳng định c
            is_c_lớn = pK_L > thresh_c
            if is_c_lớn:
                vd_da_1_d = '\\True Nếu biết nhà đầu tư sinh lời thì xác suất kinh tế đang phát triển là lớn hơn %s' % to_vn(thresh_c)
                vd_da_1_s = 'Nếu biết nhà đầu tư sinh lời thì xác suất kinh tế đang phát triển là nhỏ hơn %s' % to_vn(thresh_c)
            else:
                vd_da_1_d = '\\True Nếu biết nhà đầu tư sinh lời thì xác suất kinh tế đang phát triển là nhỏ hơn %s' % to_vn(thresh_c)
                vd_da_1_s = 'Nếu biết nhà đầu tư sinh lời thì xác suất kinh tế đang phát triển là lớn hơn %s' % to_vn(thresh_c)

            list_vd_da_1 = [vd_da_1_d, vdc_da_1_s if 'vdc_da_1_s' in locals() else vd_da_1_s]

            ######################################################################## Vận dụng cao ############################################
            # Thiết lập mệnh đề đúng / sai cho khẳng định d (Từ "chắc chắn" tương đương xác suất bằng 1, do pK_C != 1 nên luôn sai)
            vdc_da_1_d = '\\True Giả định độc lập trong cùng điều kiện kinh tế, một nhà đầu tư có lợi nhuận ở cả hai kênh bất động sản và vàng trong cùng một năm. Anh ta tin rằng điều này chưa chắc chắn chứng tỏ kinh tế đang phát triển'
            vdc_da_1_s = 'Giả định độc lập trong cùng điều kiện kinh tế, một nhà đầu tư có lợi nhuận ở cả hai kênh bất động sản và vàng trong cùng một năm. Anh ta tin rằng điều này chắc chắn chứng tỏ kinh tế đang phát triển'

            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]

            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            # Vòng lặp chọn ngẫu nhiên tổ hợp đáp án có từ 1 đến 3 câu đúng
            while True:
                nb_da_1 = random.choice(list_nb_da_1)
                th_da_1 = random.choice(list_th_da_1)
                vd_da_1 = random.choice(list_vd_da_1)
                vdc_da_1 = random.choice(list_vdc_da_1)

                answers = [nb_da_1, th_da_1, vd_da_1, vdc_da_1]
                true_count = count_true_answers(answers)

                if 1 <= true_count <= 3:
                    break

            # Đọc nhãn kết quả Đúng/Sai của phương án được chọn để đưa vào lời giải chi tiết
            lbl_a = "đúng" if '\\True' in nb_da_1 else "sai"
            lbl_b = "đúng" if '\\True' in th_da_1 else "sai"
            lbl_c = "đúng" if '\\True' in vd_da_1 else "sai"
            lbl_d = "đúng" if '\\True' in vdc_da_1 else "sai"

            # Tạo chuỗi so sánh phục vụ lời giải trực quan
            comp_a = ">" if pS_NotB > thresh_a else "<="
            comp_b = ">" if pL > thresh_b else "<="
            comp_c = ">" if pK_L > thresh_c else "<="

            # Lời giải chung giới thiệu biến cố ban đầu
            intro_loigiai = ('''Gọi $K$ là biến cố "Kinh tế phát triển"; $S$ là biến cố "Kinh tế suy thoái"; $B$ là biến cố "Đầu tư bất động sản sinh lời"; $V$ là biến cố "Đầu tư vàng sinh lời". \\\\
            Theo đề bài, ta có: $P(K) = %s$ và $P(S) = %s$. \\\\
            Khi kinh tế phát triển: $P(B|K) = %s$ và $P(V|K) = %s$. \\\\
            Khi kinh tế suy thoái: $P(B|S) = %s$ và $P(V|S) = %s$. \\\\
            Xác suất BĐS sinh lời là: $P(B) = P(B|K) \\cdot P(K) + P(B|S) \\cdot P(S) = %s \\cdot %s + %s \\cdot %s = %s$. \\\\
            Xác suất vàng sinh lời là: $P(V) = P(V|K) \\cdot P(K) + P(V|S) \\cdot P(S) = %s \\cdot %s + %s \\cdot %s = %s$.'''
            % (to_vn(pK), to_vn(pS), to_vn(pBK), to_vn(pVK), to_vn(pBS), to_vn(pVS), to_vn(pBK), to_vn(pK), to_vn(pBS), to_vn(pS), to_vn(pB), to_vn(pVK), to_vn(pK), to_vn(pVS), to_vn(pS), to_vn(pV)))

            # Nội dung lời giải chi tiết từng mục câu hỏi theo mẫu cấu trúc hệ thống
            loigiai_nb_1 = (intro_loigiai + '''Ta có: $P(\\bar{B}) = 1 - P(B) = 1 - %s = %s$ và $P(\\bar{B}|S) = 1 - P(B|S) = 1 - %s = %s$. \\\\
            Áp dụng công thức Bayes: $P(S|\\bar{B}) = \\frac{P(\\bar{B}|S) \\cdot P(S)}{P(\\bar{B})} = \\frac{%s \\cdot %s}{%s} = %s$. \\\\
            Ta thấy $%s %s %s$ nên mệnh đề a) %s.''' 
            % (to_vn(pB), to_vn(pNotB), to_vn(pBS), to_vn(pNotBS), to_vn(pNotBS), to_vn(pS), to_vn(pNotB), to_vn(pS_NotB), to_vn(pS_NotB), comp_a, to_vn(thresh_a), lbl_a))

            loigiai_th_1 = ('''Gọi $L$ là biến cố "Nhà đầu tư sinh lời". Do chọn ngẫu nhiên một trong hai kênh để đầu tư nên xác suất mỗi kênh là $0,5$. \\\\
            Khi đó: $P(L) = 0,5 \\cdot P(B) + 0,5 \\cdot P(V) = 0,5 \\cdot %s + 0,5 \\cdot %s = %s$. \\\\
            Ta thấy $%s %s %s$ nên mệnh đề b) %s.''' 
            % (to_vn(pB), to_vn(pV), to_vn(pL), to_vn(pL), comp_b, to_vn(thresh_b), lbl_b))

            loigiai_vd_1 = ('''Ta có: $P(L|K) = 0,5 \\cdot P(B|K) + 0,5 \\cdot P(V|K) = 0,5 \\cdot %s + 0,5 \\cdot %s = %s$. \\\\
            Áp dụng công thức Bayes: $P(K|L) = \\frac{P(L|K) \\cdot P(K)}{P(L)} = \\frac{%s \\cdot %s}{%s} = %s \\approx %s$. \\\\
            Ta thấy $%s %s %s$ nên mệnh đề c) %s.''' 
            % (to_vn(pBK), to_vn(pVK), to_vn(pLK), to_vn(pLK), to_vn(pK), to_vn(pL), to_frac_tex(pLK * pK / pL), to_vn(pK_L), to_vn(pK_L), comp_c, to_vn(thresh_c), lbl_c))

            loigiai_vdc_1 = ('''Gọi $C$ là biến cố "Có lợi nhuận cả hai kênh". Do giả định độc lập trong cùng điều kiện kinh tế nên: \\\\
            Khi kinh tế phát triển: $P(C|K) = P(B|K) \\cdot P(V|K) = %s \\cdot %s = %s$. \\\\
            Khi kinh tế suy thoái: $P(C|S) = P(B|S) \\cdot P(V|S) = %s \\cdot %s = %s$. \\\\
            Suy ra: $P(K|C) = \\frac{P(C|K) \\cdot P(K)}{P(C|K) \\cdot P(K) + P(C|S) \\cdot P(S)} = \\frac{%s \\cdot %s}{%s \\cdot %s + %s \\cdot %s} = %s \\approx %s \\neq 1$. \\\\
            Kết quả cho thấy khả năng kinh tế phát triển rất cao, nhưng vẫn có xác suất nhỏ là kinh tế đang suy thoái mà nhà đầu tư vẫn trúng cả hai kênh. Do đó, việc khẳng định "chắc chắn" là chưa chính xác, nên mệnh đề d) %s.''' 
            % (to_vn(pBK), to_vn(pVK), to_vn(pCK), to_vn(pBS), to_vn(pVS), to_vn(pCS), to_vn(pCK), to_vn(pK), to_vn(pCK), to_vn(pK), to_vn(pCS), to_vn(pS), to_frac_tex(pK_C), to_vn(pK_C), lbl_d))

            # Gán danh sách cuối cùng để đồng bộ minipage xuất ra TeX công cụ
            list_nb_1 = [nb_da_1]
            list_th_1 = [th_da_1]
            list_vd_1 = [vd_da_1]
            list_vdc_1 = [vdc_da_1]

            list_nb_2 = [loigiai_nb_1]
            list_th_2 = [loigiai_th_1]
            list_vd_2 = [loigiai_vd_1]
            list_vdc_2 = [loigiai_vdc_1]

            combined_nb = list(zip(list_nb_1, list_nb_2))
            combined_th = list(zip(list_th_1, list_th_2))
            combined_vd = list(zip(list_vd_1, list_vd_2))
            combined_vdc = list(zip(list_vdc_1, list_vdc_2))

            shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)
            shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)
            shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)
            shuffled_answers_vdc, shuffled_solutions_vdc = zip(*combined_vdc)

            # Thiết lập xuất mã TeX chuẩn hóa ra Console
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' +
                       str(noidungcauhoi) + '\n' +
                       '\\choiceTFn \n'
                       '{' + str(shuffled_answers_nb[0]) + '}\n'
                       '{' + str(shuffled_answers_th[0]) + '}\n'
                       '{' + str(shuffled_answers_vd[0]) + '}\n'
                       '{' + str(shuffled_answers_vdc[0]) + '}\n'
                       '\\loigiai{ \n'
                       '\\begin{enumEX}[a)]{1} \n'
                       '\\item ' + str(shuffled_solutions_nb[0]) + '\n'
                       '\\item ' + str(shuffled_solutions_th[0]) + '\n'
                       '\\item ' + str(shuffled_solutions_vd[0]) + '\n'
                       '\\item ' + str(shuffled_solutions_vdc[0]) + '\n'
                       '\\end{enumEX}} \n'
                       '\\end{ex}\n'
                       '\\end{minipage}\n\n')
            return content

