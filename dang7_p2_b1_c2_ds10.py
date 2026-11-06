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


def bt_dang7_p2_b1_c2_ds10(self):
            # Khai báo biến
            # Khai báo hàm đếm số đáp án đúng
            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            # Sinh các tham số ngẫu nhiên phù hợp với bài toán thực tế
            import random, math
            M = random.randint(10, 15)  # Số tiền tối đa (M triệu)
            A = round(random.uniform(1.5, 3.0), 1) # Giá mỗi tạ gạo
            B = round(random.uniform(1.0, 2.0), 1) # Giá mỗi tạ mì
            while A == B:
                B = round(random.uniform(1.0, 2.0), 1)

            # Format số có dấu phẩy thay vì dấu chấm theo chuẩn Toán VN
            def format_num(num):
                if num == int(num):
                    return str(int(num))
                return str(num).replace('.', ',')

            A_str = format_num(A)
            B_str = format_num(B)
            M_str = format_num(M)

            # Nội dung câu hỏi
            noidungcauhoi = (f'''Một cửa hàng dành tối đa ${M_str}$ triệu để nhập $x$ tạ gạo và $y$ tạ mì. Biết mỗi tạ gạo mua hết ${A_str}$ triệu đồng, mỗi tạ mì mua hết ${B_str}$ triệu đồng. Khi đó:''')

            ######################################################################## Nhận biết ############################################

            # Các đáp án (Đã bỏ dấu chấm ở cuối chuỗi ký tự)
            nb_da_1_d = f'\\True Số tiền (triệu đồng) mua $x$ tạ gạo và $y$ tạ mì là: ${A_str}x + {B_str}y$'
            nb_da_1_s = f'Số tiền (triệu đồng) mua $x$ tạ gạo và $y$ tạ mì là: ${B_str}x + {A_str}y$'
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]

            # Nội dung lời giải
            loigiai_nb_1 = (f'''Số tiền để mua $x$ tạ gạo là ${A_str}x$ (triệu đồng).\\\\
            Số tiền để mua $y$ tạ mì là ${B_str}y$ (triệu đồng).\\\\
            Tổng số tiền để mua gạo và mì là ${A_str}x + {B_str}y$ (triệu đồng).''')
            list_nb_2 = [loigiai_nb_1]

            ######################################################################## Thông hiểu ############################################

            # Các đáp án (Đã bỏ dấu chấm ở cuối chuỗi ký tự)
            th_da_1_d = f'\\True Bất phương trình biểu thị mối liên hệ giữa $x$ và $y$ và số tiền cửa hàng đó dành để mua gạo và mì là: ${A_str}x + {B_str}y \\le {M_str}$'
            th_da_1_s = f'Bất phương trình biểu thị mối liên hệ giữa $x$ và $y$ và số tiền cửa hàng đó dành để mua gạo và mì là: ${A_str}x + {B_str}y \\ge {M_str}$'
            list_th_da_1 = [th_da_1_d, th_da_1_s]

            # Nội dung lời giải
            loigiai_th_1 = (f'''Vì cửa hàng dành tối đa ${M_str}$ triệu đồng để mua nên tổng số tiền không được vượt quá ${M_str}$ triệu đồng.\\\\
            Do đó ta có bất phương trình: ${A_str}x + {B_str}y \\le {M_str}$.''')
            list_th_2 = [loigiai_th_1]

            ######################################################################## Vận dụng ############################################

            # Sinh ngẫu nhiên một tọa độ để kiểm tra tính đúng sai của nghiệm
            x_test = random.randint(1, 4)
            y_test = random.randint(2, 5)
            val_test = round(A * x_test + B * y_test, 2)
            is_solution = val_test <= M
            val_str = format_num(val_test)

            stmt_pos = f'Cặp $({x_test};{y_test})$ là một nghiệm của bất phương trình biểu thị mối liên hệ giữa $x$ và $y$ và số tiền cửa hàng đó dành để mua gạo và mì'
            stmt_neg = f'Cặp $({x_test};{y_test})$ không phải là một nghiệm của bất phương trình biểu thị mối liên hệ giữa $x$ và $y$ và số tiền cửa hàng đó dành để mua gạo và mì'

            if is_solution:
                vd_da_1_d = '\\True ' + stmt_pos
                vd_da_1_s = stmt_neg
            else:
                vd_da_1_d = '\\True ' + stmt_neg
                vd_da_1_s = stmt_pos

            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]

            if is_solution:
                loigiai_vd_1 = (f'''Thế $x={x_test}; y={y_test}$ vào biểu thức ta được: ${A_str} \\cdot {x_test} + {B_str} \\cdot {y_test} = {val_str} \\le {M_str}$ (đúng).\\\\
            Vậy cặp $({x_test};{y_test})$ là một nghiệm của bất phương trình.''')
            else:
                loigiai_vd_1 = (f'''Thế $x={x_test}; y={y_test}$ vào biểu thức ta được: ${A_str} \\cdot {x_test} + {B_str} \\cdot {y_test} = {val_str} > {M_str}$ (sai).\\\\
            Vậy cặp $({x_test};{y_test})$ không phải là một nghiệm của bất phương trình.''')

            list_vd_2 = [loigiai_vd_1]

            ######################################################################## Vận dụng cao ############################################

            # Các đáp án (Đã bỏ dấu chấm ở cuối chuỗi ký tự)
            vdc_da_1_d = f'\\True Miền nghiệm bất phương trình biểu thị mối liên hệ giữa $x$ và $y$ và số tiền cửa hàng đó dành để mua gạo và mì là nửa mặt phẳng bờ là đường thẳng $d: {A_str}x + {B_str}y = {M_str}$ chứa điểm $O(0;0)$'
            vdc_da_1_s = f'Miền nghiệm bất phương trình biểu thị mối liên hệ giữa $x$ và $y$ và số tiền cửa hàng đó dành để mua gạo và mì là nửa mặt phẳng bờ là đường thẳng $d: {A_str}x + {B_str}y = {M_str}$ không chứa điểm $O(0;0)$'
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]

            # Tính toán các thông số để giới hạn khung hình vẽ TikZ một cách tự động
            x_int = round(M / A, 2)
            y_int = round(M / B, 2)
            x_max_axis = math.ceil(x_int) + 3
            y_max_axis = math.ceil(y_int) + 3

            # Tính tọa độ đường thẳng d cắt các biên clip x = -2 và y = -2
            y_left = round((M + 2*A)/B, 2)
            x_bottom = round((M + 2*B)/A, 2)

            # Khởi tạo chuỗi hình vẽ TikZ động tương thích với phong cách mới
            tikz_code = f'''\\\\
            \\begin{{center}}
            \\begin{{tikzpicture}}[>=stealth, scale=0.4, line width=1pt]
            \\clip (-2,-2) rectangle ({x_max_axis},{y_max_axis});
            \\fill[pattern=north east lines, pattern color=black] (-2,-2) rectangle ({x_max_axis},{y_max_axis});
            \\fill[white] (-2,{y_left}) -- ({x_bottom},-2) -- (-2,-2) -- cycle;
            \\draw[black] (-2,{y_left}) -- ({x_bottom},-2) node[pos=0.45, sloped, above] {{}};
            \\coordinate (A) at ({x_int}, 0);
            \\coordinate (B) at (0, {y_int});
            \\fill (A) circle (3.5pt) node[above right] {{$A$}};
            \\fill (B) circle (3.5pt) node[above right] {{$B$}};
            \\draw[->] (-2, 0) -- ({x_max_axis}, 0) node[below] {{$x$}};
            \\draw[->] (0, -2) -- (0, {y_max_axis}) node[left] {{$y$}};      
            \\node at (0,0) [below left] {{$O$}};                
            \\end{{tikzpicture}}
            \\end{{center}}'''

            # Nội dung lời giải bao gồm hình vẽ sinh tự động
            loigiai_vdc_1 = (f'''Thay tọa độ điểm $O(0;0)$ vào bất phương trình ${A_str}x + {B_str}y \\le {M_str}$ ta được $0 \\le {M_str}$ (luôn đúng).\\\\
            Vậy miền nghiệm của bất phương trình là nửa mặt phẳng bờ $d: {A_str}x + {B_str}y = {M_str}$ có chứa điểm $O(0;0)$ (được biểu diễn là miền không bị gạch chéo, tính cả bờ $d$).''' + tikz_code)
            list_vdc_2 = [loigiai_vdc_1]

            ######################################################################## Xử lý Random và In ####################################

            while True:
                nb_da_1 = random.choice(list_nb_da_1)
                th_da_1 = random.choice(list_th_da_1)
                vd_da_1 = random.choice(list_vd_da_1)
                vdc_da_1 = random.choice(list_vdc_da_1)
                answers = [nb_da_1, th_da_1, vd_da_1, vdc_da_1]
                true_count = count_true_answers(answers)
                if 1 <= true_count <= 3:
                    break

            list_nb_1 = [nb_da_1]
            list_th_1 = [th_da_1]
            list_vd_1 = [vd_da_1]
            list_vdc_1 = [vdc_da_1]

            combined_nb = list(zip(list_nb_1, list_nb_2))
            combined_th = list(zip(list_th_1, list_th_2))
            combined_vd = list(zip(list_vd_1, list_vd_2))
            combined_vdc = list(zip(list_vdc_1, list_vdc_2))

            shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)
            shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)
            shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)
            shuffled_answers_vdc, shuffled_solutions_vdc = zip(*combined_vdc)

            # Xuất mã nguồn TeX hoàn chỉnh ra màn hình console
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n'+
                       str(noidungcauhoi)+ '\n' +
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

