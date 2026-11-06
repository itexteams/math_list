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


def bt_dang8_p2_b1_c2_ds10(self):
            # Khai báo biến
            # ==================== KHỞI TẠO VÀ RANDOM THAM SỐ ====================
            x, y = symbols('x y')

            # Random các thông số bài toán
            cost_noi = random.randint(1, 3)      # Giá gọi nội mạng (nghìn đồng/phút)
            cost_ngoai = random.randint(2, 4)    # Giá gọi ngoại mạng (nghìn đồng/phút)
            while cost_ngoai <= cost_noi:
                cost_ngoai = random.randint(2, 5)

            limit_money = random.choice([100, 120, 150, 200]) # Giới hạn tổng số tiền

            # Tạo ngẫu nhiên một cặp điểm để kiểm tra ở câu c
            test_x = random.choice([30, 40, 50, 60])
            test_y = random.choice([10, 20, 30])

            # Các biểu thức toán học (Tự động tối giản 1x thành x nhờ sympy)
            term_x = latex(cost_noi * x) 
            term_y = latex(cost_ngoai * y)
            expr_left = cost_noi * x + cost_ngoai * y

            is_test_correct = (cost_noi * test_x + cost_ngoai * test_y) < limit_money

            # Tọa độ giao điểm với trục tung và trục hoành
            intersect_x = Rational(limit_money, cost_noi)
            intersect_y = Rational(limit_money, cost_ngoai)

            # ==================== NỘI DUNG CÂU HỎI VÀ ĐÁP ÁN (LATEX) ====================
            noidungcauhoi = (
                f"Một công ty viễn thông tính phí ${cost_noi}$ nghìn đồng mỗi phút gọi nội mạng và ${cost_ngoai}$ nghìn đồng mỗi phút "
                f"gọi ngoại mạng. Gọi $x$ và $y$ lần lượt là số phút gọi nội mạng, ngoại mạng của Bình trong một "
                f"tháng và Bình muốn số tiền phải trả cho tổng đài luôn thấp hơn ${limit_money}$ nghìn đồng."
            )

            # ---------------------------- a) Nhận biết ----------------------------
            # ĐÃ SỬA: Xóa bỏ dấu chấm (.) ở cuối các đáp án hỏi
            nb_da_1_d = (f"\\True Số tiền phải trả cho cuộc gọi nội mạng mỗi tháng là ${term_x}$ (nghìn đồng), "
                         f"số tiền phải trả cho cuộc gọi ngoại mạng mỗi tháng là ${term_y}$ (nghìn đồng). "
                         f"Điều kiện: $x \\in \\mathbb{{N}}, y \\in \\mathbb{{N}}$")
            nb_da_1_s = (f"Số tiền phải trả cho cuộc gọi nội mạng mỗi tháng là ${term_y}$ (nghìn đồng), "
                         f"số tiền phải trả cho cuộc gọi ngoại mạng mỗi tháng là ${term_x}$ (nghìn đồng). "
                         f"Điều kiện: $x \\in \\mathbb{{R}}, y \\in \\mathbb{{R}}$")
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]

            # Lời giải vẫn cần dấu chấm để kết thúc câu hoàn chỉnh
            loigiai_nb_1 = (f"Số tiền phải trả cho cuộc gọi nội mạng mỗi tháng là ${term_x}$ (nghìn đồng), "
                            f"số tiền phải trả cho cuộc gọi ngoại mạng mỗi tháng là ${term_y}$ (nghìn đồng). "
                            f"Do số phút phải là số tự nhiên nên điều kiện: $x \\in \\mathbb{{N}}, y \\in \\mathbb{{N}}$.")

            # ---------------------------- b) Thông hiểu ----------------------------
            # ĐÃ SỬA: Xóa bỏ dấu chấm (.) ở cuối các đáp án hỏi
            th_da_1_d = f"\\True Bất phương trình bậc nhất gồm hai ẩn số $x,y$ đã cho là ${latex(expr_left)} < {limit_money}$"
            th_da_1_s = f"Bất phương trình bậc nhất gồm hai ẩn số $x,y$ đã cho là ${latex(expr_left)} \\le {limit_money}$"
            list_th_da_1 = [th_da_1_d, th_da_1_s]

            loigiai_th_1 = (f"Tổng số tiền Bình phải trả là ${latex(expr_left)}$ (nghìn đồng). "
                            f"Vì số tiền thấp hơn ${limit_money}$ nghìn đồng nên ta có bất phương trình: ${latex(expr_left)} < {limit_money}$ (*).")

            # ---------------------------- c) Vận dụng ----------------------------
            # ĐÃ SỬA: Xóa bỏ dấu chấm (.) ở cuối các đáp án hỏi
            if is_test_correct:
                vd_da_1_d = f"\\True $x = {test_x}, y = {test_y}$ là một nghiệm của bất phương trình bậc nhất gồm hai ẩn số $x,y$ đã cho"
                vd_da_1_s = f"$x = {test_x}, y = {test_y}$ không phải là nghiệm của bất phương trình bậc nhất gồm hai ẩn số $x,y$ đã cho"
            else:
                vd_da_1_d = f"\\True $x = {test_x}, y = {test_y}$ không phải là nghiệm của bất phương trình bậc nhất gồm hai ẩn số $x,y$ đã cho"
                vd_da_1_s = f"$x = {test_x}, y = {test_y}$ là một nghiệm của bất phương trình bậc nhất gồm hai ẩn số $x,y$ đã cho"
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]

            calc_value = cost_noi * test_x + cost_ngoai * test_y
            status_str = "đúng" if is_test_correct else "sai"
            conclusion_str = "là một nghiệm" if is_test_correct else "không phải là nghiệm"

            loigiai_vd_1 = (f"Xét $x = {test_x}, y = {test_y}$, thay vào (*) ta được: "
                            f"${cost_noi} \\cdot {test_x} + {cost_ngoai} \\cdot {test_y} < {limit_money} \\Leftrightarrow {calc_value} < {limit_money}$ ({status_str}), "
                            f"suy ra $({test_x}; {test_y})$ {conclusion_str} của (*).")

            # ---------------------------- d) Vận dụng cao ----------------------------
            # ĐÃ SỬA: Xóa bỏ dấu chấm (.) ở cuối các đáp án hỏi
            vdc_da_1_d = "Miền nghiệm của bất phương trình bậc nhất gồm hai ẩn số $x,y$ đã cho là một hình vuông"
            vdc_da_1_s = "\\True Miền nghiệm của bất phương trình bậc nhất gồm hai ẩn số $x,y$ đã cho là một miền tam giác"
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]

            # ---- Bảng giá trị ----
            table_latex = f"""\\begin{{center}}
            \\begin{{tabular}}{{|c|c|c|}}
            \\hline
            $x$ & $0$ & ${latex(intersect_x)}$ \\\\ 
            \\hline
            $y$ & ${latex(intersect_y)}$ & $0$ \\\\ 
            \\hline
            \\end{{tabular}}
            \\end{{center}}"""

            # ---- Hình vẽ TikZ miền nghiệm theo phong cách mới ----
            # Sử dụng tọa độ ảo cố định để khung hình luôn đẹp bất kể limit_money lớn mức nào,
            # kết hợp phương pháp clip, pattern và fill white cho miền nghiệm
            tikz_latex = f"""\\begin{{center}}
            \\begin{{tikzpicture}}[>=stealth, scale=0.4, line width=1pt]
            \\clip (-2,-2) rectangle (8,7);
            \\fill[pattern=north east lines, pattern color=black] (-2,-2) rectangle (8,7);
            \\fill[white] (-2, 5.6) -- (7.5, -2) -- (-2, -2) -- cycle;
            \\draw[dashed, black] (-2, 5.6) -- (7.5, -2);
            \\coordinate (A) at (0, 4);
            \\coordinate (B) at (5, 0);
            \\fill (A) circle (3.5pt) node[above right] {{$A$}} node[left] {{${latex(intersect_y)}$}};
            \\fill (B) circle (3.5pt) node[above right] {{$B$}} node[below] {{${latex(intersect_x)}$}};
            \\draw[->] (-2, 0) -- (8, 0) node[below] {{$x$}};
            \\draw[->] (0, -2) -- (0, 7) node[left] {{$y$}};
            \\node at (0,0) [below left] {{$O$}};                
            \\end{{tikzpicture}}
            \\end{{center}}"""

            loigiai_vdc_1 = (
                f"Biểu diễn miền nghiệm của $(*)$ trên hệ trục tọa độ: Vẽ đường thẳng $d: {latex(expr_left)} = {limit_money}$ theo bảng giá trị:\\\\ \n"
                f"{table_latex}\n"
                f"Ta thấy điểm $O(0;0)$ thuộc miền nghiệm của $(*)$ do thay tọa độ $O$ vào $(*): 0 < {limit_money}$ (đúng).\\\\ \n"
                f"Vậy miền nghiệm của bất phương trình $(*): {latex(expr_left)} < {limit_money}$ là nửa mặt phẳng (không kể $d$) có chứa điểm $O$ (phần không gạch chéo trên hình).\n"
                f"{tikz_latex}\n"
                f"Vì $x \\in \\mathbb{{N}}, y \\in \\mathbb{{N}}$ nên ta chỉ xét các điểm có tọa độ nguyên nằm trong miền tam giác $OAB$ tạo bởi đường thẳng và hai trục tọa độ. \n"
                f"Do đó miền nghiệm là một hình tam giác."
            )

            # ==================== VÒNG LẶP ĐẢM BẢO SỐ ĐÁP ÁN ĐÚNG ====================
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

            # Gán trộn
            combined_nb = list(zip([nb_da_1], [loigiai_nb_1]))
            combined_th = list(zip([th_da_1], [loigiai_th_1]))
            combined_vd = list(zip([vd_da_1], [loigiai_vd_1]))
            combined_vdc = list(zip([vdc_da_1], [loigiai_vdc_1]))

            shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)
            shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)
            shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)
            shuffled_answers_vdc, shuffled_solutions_vdc = zip(*combined_vdc)

            # ==================== TRÍCH XUẤT ĐẦU RA ====================
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
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

