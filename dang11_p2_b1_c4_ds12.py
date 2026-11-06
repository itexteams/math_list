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


def bt_dang11_p2_b1_c4_ds12(self):
            # Khai báo biến
            # Hàm hỗ trợ định dạng số thập phân dùng dấu phẩy
            def f_num(val):
                return str(round(float(val), 4)).replace('.', ',')

            # --- BƯỚC 1: NGẪU NHIÊN CÁC THÔNG SỐ CƠ BẢN ---
            # Xác suất trời mưa
            p_rain = random.choice([0.2, 0.3, 0.4])
            p_no_rain = round(1 - p_rain, 1)

            # Xác suất An đi xem
            p_a_given_nr = random.choice([0.7, 0.8]) # An đi nếu không mưa
            p_a_given_r = random.choice([0.4, 0.5])  # An đi nếu mưa

            # Xác suất Bảo đi (phụ thuộc An)
            p_b_given_a = random.choice([0.8, 0.9])  # Bảo đi nếu An đi

            # Xác suất Châu đi (độc lập)
            p_c = random.choice([0.5, 0.6, 0.7])
            p_not_c = round(1 - p_c, 1)

            # --- BƯỚC 2: TÍNH TOÁN CÁC GIÁ TRỊ ĐÁP ÁN ĐÚNG ---

            # a) Xác suất An không đi nếu trời không mưa
            ans_a_true_val = round(1 - p_a_given_nr, 2)

            # b) Xác suất An đi xem bóng đá (Xác suất đầy đủ)
            # P(A) = P(R).P(A|R) + P(!R).P(A|!R)
            p_a = round(p_rain * p_a_given_r + p_no_rain * p_a_given_nr, 4)
            p_not_a = round(1 - p_a, 4)

            # c) Xác suất Bảo không đi xem bóng đá
            # P(!B) = P(A).P(!B|A) + P(!A).P(!B|!A)
            # P(!B|!A) = 1 (vì An không đi thì Bảo chắc chắn không đi)
            p_not_b_given_a = round(1 - p_b_given_a, 1)
            p_not_b = round(p_a * p_not_b_given_a + p_not_a * 1, 4)

            # d) Xác suất ít nhất 2 người đi
            # Các trường hợp: (An, Bảo, !Châu), (An, !Bảo, Châu), (An, Bảo, Châu)
            # Lưu ý: Bảo chỉ đi khi An đi, nên không có trường (!An, Bảo, Châu)
            p1 = round(p_a * p_b_given_a * p_not_c, 4)
            p2 = round(p_a * (1 - p_b_given_a) * p_c, 4)
            p3 = round(p_a * p_b_given_a * p_c, 4)
            p_at_least_2 = round(p1 + p2 + p3, 4)

            # --- BƯỚC 3: XÂY DỰNG NỘI DUNG CÂU HỎI ---

            noidungcauhoi = ('''Ba người bạn An, Bảo và Châu đều muốn đi xem một trận bóng đá. Khả năng mỗi người đi được phụ thuộc vào các yếu tố sau:\\\\
            An: Nếu trời không mưa, An có %s\\%% khả năng đi xem bóng đá. Nếu trời mưa, khả năng này giảm xuống còn %s\\%%. Theo dự báo thời tiết, khả năng trời mưa trong ngày diễn ra trận đấu là %s\\%%. Việc An đi xem bóng đá hoàn toàn phụ thuộc vào thời tiết.\\\\
            Bảo: Việc Bảo đi xem bóng đá hoàn toàn phụ thuộc vào việc An có đi hay không. Nếu An đi, Bảo có %s\\%% khả năng đi. Nếu An không đi, Bảo chắc chắn sẽ không đi.\\\\
            Châu: Châu là một người rất độc lập. Khả năng Châu đi xem bóng đá không phụ thuộc vào việc An và Bảo có đi hay không. Châu có %s\\%% khả năng đi xem bóng đá.''' 
            % (int(p_a_given_nr*100), int(p_a_given_r*100), int(p_rain*100), int(p_b_given_a*100), int(p_c*100)))

            # --- BƯỚC 4: NHẬN BIẾT (Câu a) ---
            nb_da_1_d = '\\True Nếu trời không mưa, khả năng An không đi xem bóng đá là %s\\%%' % (int(ans_a_true_val*100))
            nb_da_1_s = 'Nếu trời không mưa, khả năng An không đi xem bóng đá là %s\\%%' % (int(p_a_given_nr*100))
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            loigiai_nb_1 = ('''Nếu trời không mưa khả năng An không đi xem bóng đá là $100\\%% - %s\\%% = %s\\%%$.''' 
                            % (int(p_a_given_nr*100), int(ans_a_true_val*100)))

            # --- BƯỚC 5: THÔNG HIỂU (Câu b) ---
            th_da_1_d = '\\True Xác suất An đi xem đá bóng là %s' % (f_num(p_a))
            th_da_1_s = 'Xác suất An đi xem đá bóng là %s' % (f_num(p_a + 0.05))
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            loigiai_th_1 = ('''Xác suất An đi xem bóng đá là: $P = %s \\cdot %s + %s \\cdot %s = %s$.''' 
                            % (f_num(p_rain), f_num(p_a_given_r), f_num(p_no_rain), f_num(p_a_given_nr), f_num(p_a)))

            # --- BƯỚC 6: VẬN DỤNG (Câu c) ---
            c_sai_val = round(p_not_b - 0.002, 3) # Tạo giá trị sai gần giống kết quả đúng
            vd_da_1_d = '\\True Xác suất Bảo không đi xem đá bóng là %s' % (f_num(p_not_b))
            vd_da_1_s = 'Xác suất Bảo không đi xem đá bóng là %s' % (f_num(c_sai_val))
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            loigiai_vd_1 = ('''Có hai trường hợp Bảo không đi: \\\\
            - An đi, Bảo không đi. \\\\
            - An không đi, Bảo chắc chắn không đi. \\\\
            Xác suất là: $P = %s \\cdot %s + %s = %s$.''' 
                            % (f_num(p_a), f_num(p_not_b_given_a), f_num(p_not_a), f_num(p_not_b)))

            # --- BƯỚC 7: VẬN DỤNG CAO (Câu d) ---
            vdc_da_1_d = '\\True Xác suất để ít nhất hai trong ba người bạn cùng đi xem trận bóng đá là %s' % (f_num(p_at_least_2))
            vdc_da_1_s = 'Xác suất để ít nhất hai trong ba người bạn cùng đi xem trận bóng đá là %s' % (f_num(p_at_least_2 - 0.01))
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            loigiai_vdc_1 = ('''Có ít nhất hai người bạn đi xem bóng đá: \\\\
            - An, Bảo đi, Châu không đi: $p_1 = %s \\cdot %s \\cdot %s = %s$. \\\\
            - An, Châu đi, Bảo không đi: $p_2 = %s \\cdot %s \\cdot %s = %s$. \\\\
            - An, Bảo, Châu đi: $p_3 = %s \\cdot %s \\cdot %s = %s$. \\\\
            Vậy xác suất cần tìm là $P = p_1 + p_2 + p_3 = %s$.''' 
                             % (f_num(p_a), f_num(p_b_given_a), f_num(p_not_c), f_num(p1),
                                f_num(p_a), f_num(p_c), f_num(p_not_b_given_a), f_num(p2),
                                f_num(p_a), f_num(p_b_given_a), f_num(p_c), f_num(p3),
                                f_num(p_at_least_2)))

            # --- BƯỚC 8: VÒNG LẶP CHỌN ĐÁP ÁN (1-3 ĐÚNG) ---
            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            while True:
                nb_da_1 = random.choice(list_nb_da_1)
                th_da_1 = random.choice(list_th_da_1)
                vd_da_1 = random.choice(list_vd_da_1)
                vdc_da_1 = random.choice(list_vdc_da_1)

                answers = [nb_da_1, th_da_1, vd_da_1, vdc_da_1]
                true_count = count_true_answers(answers)
                if 1 <= true_count <= 3:
                    break

            # Trộn và chuẩn bị xuất bản
            list_nb_2 = [loigiai_nb_1]
            list_th_2 = [loigiai_th_1]
            list_vd_2 = [loigiai_vd_1]
            list_vdc_2 = [loigiai_vdc_1]

            # Xuất nội dung
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + 
                str(noidungcauhoi) + '\n'
                '\\choiceTFn \n'
                '{' + str(nb_da_1) + '}\n'
                '{' + str(th_da_1) + '}\n'
                '{' + str(vd_da_1) + '}\n'
                '{' + str(vdc_da_1) + '}\n'
                '\\loigiai{ \n'
                '\\begin{enumEX}[a)]{1} \n'
                '\\item ' + str(loigiai_nb_1) + '\n'
                '\\item ' + str(loigiai_th_1) + '\n'
                '\\item ' + str(loigiai_vd_1) + '\n'
                '\\item ' + str(loigiai_vdc_1) + '\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

