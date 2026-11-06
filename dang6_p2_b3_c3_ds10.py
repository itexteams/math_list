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


def bt_dang6_p2_b3_c3_ds10(self):
            # Khai báo biến
            # Khai báo hàm đếm số đáp án đúng
            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            # Định dạng số thập phân dùng dấu phẩy của Việt Nam
            def format_num(num):
                # Vì chia 5 hoặc 25 nên phần thập phân tối đa 2 chữ số, an toàn để round(num, 2)
                res = f"{round(num, 2):g}"
                return res.replace('.', ',')

            ######################################################################## Xử lý Data Random ########################

            # Sinh ngẫu nhiên dữ liệu 5 cây cho Hưng (Đồng đều hơn -> Biên độ dao động nhỏ)
            base_H = random.randint(32, 38)
            data_H = [base_H + random.randint(-2, 2) for _ in range(5)]

            # Sinh ngẫu nhiên dữ liệu 5 cây cho Thịnh (Phân tán hơn -> Biên độ dao động lớn)
            base_T = random.randint(30, 40)
            data_T = [base_T + random.randint(-6, 7) for _ in range(5)]

            # Tính toán các đại lượng thống kê
            n = 5
            mean_H = sum(data_H) / n
            mean_T = sum(data_T) / n

            var_H = sum((x - mean_H)**2 for x in data_H) / n
            var_T = sum((x - mean_T)**2 for x in data_T) / n

            # Đảm bảo phương sai của Hưng luôn nhỏ hơn Thịnh để khớp logic cố định của bài (hoặc tráo đổi nếu cần)
            if var_H >= var_T:
                data_H, data_T = data_T, data_H
                mean_H, mean_T = mean_T, mean_H
                var_H, var_T = var_T, var_H

            # Format chuỗi dữ liệu
            mean_H_str = format_num(mean_H)
            mean_T_str = format_num(mean_T)
            var_H_str = format_num(var_H)
            var_T_str = format_num(var_T)

            # Nội dung câu hỏi
            noidungcauhoi = f'''Bạn Hưng và bạn Thịnh thống kê kết quả chiều cao (đơn vị: xăng-ti-mét) của 5 cây nguyệt quế mà mỗi người trồng sau một thời gian như sau:
            \\begin{{center}}
            \\begin{{tabular}}{{|l|c|c|c|c|c|}}
            \\hline
            Cây của bạn Hưng & {data_H[0]} & {data_H[1]} & {data_H[2]} & {data_H[3]} & {data_H[4]} \\\\
            \\hline
            Cây của bạn Thịnh & {data_T[0]} & {data_T[1]} & {data_T[2]} & {data_T[3]} & {data_T[4]} \\\\
            \\hline
            \\end{{tabular}}
            \\end{{center}}'''

            ######################################################################## Nhận biết ############################################

            # Tạo đáp án sai ngẫu nhiên cho Hưng
            mean_H_fake = mean_H + random.choice([-1.2, 1.4, 2.0, -0.8])
            mean_H_fake_str = format_num(mean_H_fake)

            # Các đáp án
            nb_da_1_d = f'\\True Số trung bình cộng của mẫu số liệu cây của bạn Hưng là: $\\overline{{x}}_H = {mean_H_str}(cm)$'
            nb_da_1_s = f'Số trung bình cộng của mẫu số liệu cây của bạn Hưng là: $\\overline{{x}}_H = {mean_H_fake_str}(cm)$'
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]

            # Nội dung lời giải
            sum_H_str = " + ".join(map(str, data_H))
            loigiai_nb_1 = (f"Mẫu số liệu chiều cao 5 cây do bạn Hưng trồng là: {', '.join(map(str, data_H))}.\\\\"
                            f"Số trung bình cộng của mẫu số liệu này là: $\\overline{{x}}_H = \\frac{{{sum_H_str}}}{{5}} = {mean_H_str}(cm)$.")
            list_nb_2 = [loigiai_nb_1]

            ######################################################################## Thông hiểu ############################################

            # Tạo đáp án sai ngẫu nhiên cho Thịnh
            mean_T_fake = mean_T + random.choice([-2.4, 1.6, 2.2, -1.8])
            mean_T_fake_str = format_num(mean_T_fake)

            # Các đáp án
            th_da_1_d = f'\\True Số trung bình cộng của mẫu số liệu cây của bạn Thịnh là: $\\overline{{x}}_T = {mean_T_str}(cm)$'
            th_da_1_s = f'Số trung bình cộng của mẫu số liệu cây của bạn Thịnh là: $\\overline{{x}}_T = {mean_T_fake_str}(cm)$'
            list_th_da_1 = [th_da_1_d, th_da_1_s]

            # Nội dung lời giải
            sum_T_str = " + ".join(map(str, data_T))
            loigiai_th_1 = (f"Mẫu số liệu chiều cao 5 cây do bạn Thịnh trồng là: {', '.join(map(str, data_T))}.\\\\"
                            f"Số trung bình cộng của mẫu số liệu này là: $\\overline{{x}}_T = \\frac{{{sum_T_str}}}{{5}} = {mean_T_str}(cm)$.")
            list_th_2 = [loigiai_th_1]

            ######################################################################## Vận dụng ############################################

            # Bẫy mệnh đề (Vì var_H < var_T, mệnh đề "lớn hơn" sẽ là SAI, "nhỏ hơn" sẽ là ĐÚNG)
            vd_da_1_d = '\\True Phương sai của mẫu số liệu cây của bạn Hưng \\textbf{nhỏ hơn} Phương sai của mẫu số liệu cây của bạn Thịnh'
            vd_da_1_s = 'Phương sai của mẫu số liệu cây của bạn Hưng \\textbf{lớn hơn} Phương sai của mẫu số liệu cây của bạn Thịnh'
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]

            # Nội dung lời giải
            loigiai_vd_1 = (f"Phương sai của mẫu số liệu cây của bạn Hưng là: $s_H^2 = {var_H_str}$.\\\\"
                            f"Phương sai của mẫu số liệu cây của bạn Thịnh là: $s_T^2 = {var_T_str}$.\\\\"
                            f"Vì $s_H^2 < s_T^2$ nên phương sai của mẫu số liệu cây của bạn Hưng nhỏ hơn.")
            list_vd_2 = [loigiai_vd_1]

            ######################################################################## Vận dụng cao ########################################

            vdc_da_1_d = '\\True Các cây nguyệt quế của bạn Hưng phát triển chiều cao đồng đều hơ.'
            vdc_da_1_s = 'Các cây nguyệt quế của bạn Thịnh phát triển chiều cao đồng đều hơn'
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]

            # Nội dung lời giải
            loigiai_vdc_1 = (f"Vì phương sai mẫu số liệu của bạn Hưng nhỏ hơn ($s_H^2 < s_T^2$) "
                             f"nên các cây nguyệt quế của bạn Hưng phát triển chiều cao đồng đều hơn.")
            list_vdc_2 = [loigiai_vdc_1]

            ######################################################################## Xáo trộn và in kết quả ###############################

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
                '\\end{ex}\n'
                '\\end{minipage}\n\n')
            return content

