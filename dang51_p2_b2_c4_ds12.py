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


def bt_dang51_p2_b2_c4_ds12(self):
            # Khai báo biến
            # Định nghĩa hàm format phần trăm (Đổi dấu . thành , cho số thập phân)
            def format_pct(val):
                val = round(float(val), 2)
                if val.is_integer():
                    return str(int(val))
                return str(val).replace('.', ',')

            # Khởi tạo các số ngẫu nhiên cho bài toán
            # Tổng số bi = tong_do + tong_vang
            while True:
                tong_do = random.choice([40, 50, 60])
                tong_vang = random.choice([20, 30, 40])
                tong_bi = tong_do + tong_vang

                pct_do_danhso = random.choice([40, 60, 80]) # phần trăm bi đỏ được đánh số
                pct_vang_danhso = random.choice([30, 50, 70]) # phần trăm bi vàng được đánh số

                # Tính số lượng bi để kiểm tra tính nguyên vẹn
                do_danhso = (tong_do * pct_do_danhso) // 100
                vang_danhso = (tong_vang * pct_vang_danhso) // 100

                # Tính các xác suất thành phần 
                p_an = (tong_do / tong_bi) * 100
                p_bn_vang_ds = (tong_vang / tong_bi) * (pct_vang_danhso / 100) * 100
                p_b_ds = ((tong_do * pct_do_danhso + tong_vang * pct_vang_danhso) / tong_bi)
                p_cn_khong_ds = 100 - p_b_ds

                # Kiểm tra điều kiện số đẹp (không quá nhiều chữ số thập phân vô hạn)
                if (p_an == int(p_an) or (p_an * 10) % 1 == 0 or (p_an * 100) % 1 == 0) and \
                   (p_bn_vang_ds == int(p_bn_vang_ds) or (p_bn_vang_ds * 10) % 1 == 0 or (p_bn_vang_ds * 100) % 1 == 0):
                    break

            # Gán các chuỗi hiển thị sau khi đã chuẩn hóa
            p_a_str = format_pct(p_an)
            p_not_a_str = format_pct(100 - p_an)

            pct_do_ds_str = format_pct(pct_do_danhso)
            pct_vang_ds_str = format_pct(pct_vang_danhso)

            p_b_str = format_pct(p_b_ds)
            p_not_b_str = format_pct(p_cn_khong_ds)
            p_vang_and_b_str = format_pct(p_bn_vang_ds)

            # Tính xác suất có điều kiện cho câu d
            do_khong_danhso = tong_do * (100 - pct_do_danhso) / 100
            vang_khong_danhso = tong_vang * (100 - pct_vang_danhso) / 100

            p_cond_do = do_khong_danhso / (do_khong_danhso + vang_khong_danhso)
            p_cond_vang = vang_khong_danhso / (do_khong_danhso + vang_khong_danhso)

            frac_do = Rational(int(do_khong_danhso), int(do_khong_danhso + vang_khong_danhso))
            frac_vang = Rational(int(vang_khong_danhso), int(do_khong_danhso + vang_khong_danhso))

            if p_cond_do > p_cond_vang:
                sanh_cum = "cao hơn"
                sanh_cum_sai = "thấp hơn"
            else:
                sanh_cum = "thấp hơn"
                sanh_cum_sai = "cao hơn"

            # Nội dung câu hỏi
            noidungcauhoi = ('''Một hộp có %s viên bi, trong đó có %s viên bi màu đỏ và %s viên bi màu vàng. Các viên bi có kích thước và khối lượng như nhau. Sau khi kiểm tra, người ta thấy có %s\\%% số viên bi màu đỏ đánh số và %s\\%% số viên bi màu vàng có đánh số, những viên bi còn lại không đánh số. Lấy ra ngẫu nhiên 1 viên bi trong hộp.''' 
                             %(latex(tong_bi), latex(tong_do), latex(tong_vang), pct_do_ds_str, pct_vang_ds_str))

            ########################################################################
            # Nhận biết 
            # Các đáp án
            nb_da_1_d = '\\True Xác suất chọn được viên bi màu đỏ bằng %s\\%%' %(p_a_str)
            nb_da_1_s = 'Xác suất chọn được viên bi màu đỏ bằng %s\\%%' %(format_pct(p_an + 5))
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)

            # Danh sách chọn ngẫu nhiên
            list_nb_1 = [nb_da_1]

            # Nội dung lời giải
            loigiai_nb_1 = ('''Xác suất chọn được viên bi màu đỏ là $P(A) = \\frac{%s}{%s} = %s\\%%$.'''
                            %(latex(tong_do), latex(tong_bi), p_a_str))

            list_nb_2 = [loigiai_nb_1]
            combined_nb = list(zip(list_nb_1, list_nb_2))
            random.shuffle(combined_nb)
            shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)

            ########################################################################
            # Thông hiểu
            # Các đáp án
            th_da_1_d = '\\True Xác suất chọn được viên bi màu vàng có đánh số bằng %s\\%%' %(p_vang_and_b_str)
            th_da_1_s = 'Xác suất chọn được viên bi màu vàng có đánh số bằng %s\\%%' %(format_pct(p_bn_vang_ds - 2.5))
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)

            list_th_1 = [th_da_1]

            # Nội dung lời giải
            loigiai_th_1 = ('''Ta có $P(\\overline{A}) = \\frac{%s}{%s} = %s\\%%$, $P(B|\\overline{A}) = %s\\%%$.\\\\Xác suất chọn được viên bi màu vàng đã được đánh số là \\\\$P(\\overline{A} \\cap B) = P(\\overline{A}) \\cdot P(B|\\overline{A}) = %s\\%% \\cdot %s\\%% = %s\\%%$.''' 
                            %(latex(tong_vang), latex(tong_bi), p_not_a_str, pct_vang_ds_str, p_not_a_str, pct_vang_ds_str, p_vang_and_b_str))

            list_th_2 = [loigiai_th_1]
            combined_th = list(zip(list_th_1, list_th_2))
            random.shuffle(combined_th)
            shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)

            ########################################################################
            # Vận dụng
            # Các đáp án
            vd_da_1_d = '\\True Xác suất chọn được viên bi không đánh số bằng %s\\%%' %(p_not_b_str)
            vd_da_1_s = 'Xác suất chọn được viên bi không đánh số bằng %s\\%%' %(format_pct(p_cn_khong_ds + 3.5))
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)

            list_vd_1 = [vd_da_1]

            # Nội dung lời giải
            loigiai_vd_1 = ('''Xác suất chọn được viên bi đã được đánh số là $P(B) = P(A) \\cdot P(B|A) + P(\\overline{A}) \\cdot P(B|\\overline{A}) = %s\\%% \\cdot %s\\%% + %s\\%% \\cdot %s\\%% = %s\\%%$.\\\\Suy ra xác suất chọn được viên bi chưa đánh số là \\\\$P(\\overline{B}) = 1 - P(B) = %s\\%%$.''' 
                            %(p_a_str, pct_do_ds_str, p_not_a_str, pct_vang_ds_str, p_b_str, p_not_b_str))

            list_vd_2 = [loigiai_vd_1]
            combined_vd = list(zip(list_vd_1, list_vd_2))
            random.shuffle(combined_vd)
            shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)

            ########################################################################
            # Vận dụng cao
            # Các đáp án
            vdc_da_1_d = '\\True Giả sử viên bi được lấy ra là viên bi chưa được đánh số, xác suất để viên bi đó là bi đỏ %s xác suất viên bi đó là bi vàng' %(sanh_cum)
            vdc_da_1_s = 'Giả sử viên bi được lấy ra là viên bi chưa được đánh số, xác suất để viên bi đó là bi đỏ %s xác suất viên bi đó là bi vàng' %(sanh_cum_sai)
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)

            list_vdc_1 = [vdc_da_1]

            # Nội dung lời giải
            loigiai_vdc_1 = ('''Giả sử viên bi được lấy ra là viên bi chưa được đánh số. Khi đó:\\\\Xác suất để viên bi đó là bi đỏ: $P(A|\\overline{B}) = \\frac{P(A) \\cdot P(\\overline{B}|A)}{P(\\overline{B})} = \\frac{%s\\%% \\cdot (1 - %s\\%%)}{%s\\%%} = %s$.\\\\Xác suất để viên bi đó là bi vàng: $P(\\overline{A}|\\overline{B}) = \\frac{P(\\overline{A}) \\cdot P(\\overline{B}|\\overline{A})}{P(\\overline{B})} = \\frac{%s\\%% \\cdot (1 - %s\\%%)}{%s\\%%} = %s$.\\\\Vậy xác suất viên bi đó là bi đỏ %s xác suất viên bi đó là bi vàng.''' 
                             %(p_a_str, pct_do_ds_str, p_not_b_str, latex(frac_do), p_not_a_str, pct_vang_ds_str, p_not_b_str, latex(frac_vang), sanh_cum))

            list_vdc_2 = [loigiai_vdc_1]
            combined_vdc = list(zip(list_vdc_1, list_vdc_2))
            random.shuffle(combined_vdc)
            shuffled_answers_vdc, shuffled_solutions_vdc = zip(*combined_vdc)

            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            # Lặp đến khi đáp án có từ 1 đến 3 câu đúng
            while True:
                nb_da_1 = random.choice(list_nb_da_1)
                th_da_1 = random.choice(list_th_da_1)
                vd_da_1 = random.choice(list_vd_da_1)
                vdc_da_1 = random.choice(list_vdc_da_1)

                answers = [nb_da_1, th_da_1, vd_da_1, vdc_da_1]
                true_count = count_true_answers(answers)

                if 1 <= true_count <= 3:
                    break

            # Gán lại vào list sau khi lọc số lượng câu đúng hợp lệ
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
                str(noidungcauhoi)+ 
                ' \n\\choiceTFn \n'
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

