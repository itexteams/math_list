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


def bt_dang5_p2_b1_c2_ds10(self):
            # Khai báo biến
            # =========================================================================
            contexts = [
                {"name": "rạp chiếu phim", "item": "bộ phim hoạt hình", "type1": "Trẻ em", "type2": "Người lớn"},
                {"name": "sân vận động", "item": "trận bóng đá", "type1": "Học sinh", "type2": "Khán giả tự do"},
                {"name": "nhà hát", "item": "đêm nhạc", "type1": "Vé phổ thông", "type2": "Vé VIP"}
            ]

            ctx = random.choice(contexts)
            v1 = random.randrange(40000, 70000, 10000)
            v2 = random.randrange(80000, 130000, 10000)
            target_trieu = random.randint(15, 30)
            target_dong = target_trieu * 1000000

            # Rút gọn hệ số (chia cho 1000)
            k1, k2, kt = v1//1000, v2//1000, target_dong//1000

            # Điểm kiểm tra cho câu Vận dụng
            x0 = random.randrange(100, 400, 50)
            y0 = random.randrange(100, 400, 50)
            check_val = v1 * x0 + v2 * y0
            is_sol = (check_val >= target_dong)

            # Nội dung câu hỏi
            noidungcauhoi = (f"Nhân dịp Trung thu, một {ctx['name']} phục vụ khán giả {ctx['item']}. "
                             f"Vé bán ra có hai loại: Loại 1 ({ctx['type1']}) giá ${v1}$ đồng/vé; "
                             f"Loại 2 ({ctx['type2']}) giá ${v2}$ đồng/vé. "
                             f"Để không phải bù lỗ, số tiền vé thu được phải đạt tối thiểu ${target_trieu}$ triệu đồng. "
                             f"Gọi $x, y$ lần lượt là số vé loại 1 và loại 2 bán được.")

            ########################################################################
            # Nhận biết ############################################
            nb_da_1_d = f'\\True Số tiền bán vé loại 1 là ${v1}x$, số tiền bán vé loại 2 là ${v2}y$ ($x, y \\ge 0$)'
            nb_da_1_s = f'Số tiền bán vé loại 1 là ${v2}x$, số tiền bán vé loại 2 là ${v1}y$ ($x, y \\ge 0$)'
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)
            list_nb_1 = [nb_da_1]
            loigiai_nb_1 = f"Số tiền thu được bằng đơn giá nhân số lượng. Vậy tổng số tiền là ${v1}x + {v2}y$."
            list_nb_2 = [loigiai_nb_1]

            ########################################################################
            # Thông hiểu ############################################
            th_da_1_d = f'\\True Bất phương trình mô tả điều kiện không lỗ là ${k1}x + {k2}y \\ge {kt}$'
            th_da_1_s = f'Bất phương trình mô tả điều kiện không lỗ là ${k1}x + {k2}y \\le {kt}$'
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)
            list_th_1 = [th_da_1]
            loigiai_th_1 = f"Để không lỗ, doanh thu phải $\\ge {target_dong}$. Ta có: ${v1}x + {v2}y \\ge {target_dong} \\Leftrightarrow {k1}x + {k2}y \\ge {kt}$."
            list_th_2 = [loigiai_th_1]

            ########################################################################
            # Vận dụng ############################################
            vd_da_1_d = f"\\True Cặp số $({x0}; {y0})$ {'là' if is_sol else 'không là'} nghiệm của bất phương trình"
            vd_da_1_s = f"Cặp số $({x0}; {y0})$ {'không là' if is_sol else 'là'} nghiệm của bất phương trình"
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)
            list_vd_1 = [vd_da_1]
            loigiai_vd_1 = (f"Thay $x={x0}, y={y0}$ vào VT: ${k1} \\cdot {x0} + {k2} \\cdot {y0} = {k1*x0 + k2*y0}$. "
                            f"So với ${kt}$, ta thấy cặp số {'thỏa mãn' if is_sol else 'không thỏa mãn'} BPT.")
            list_vd_2 = [loigiai_vd_1]

            ########################################################################
            # Vận dụng cao ############################################
            vdc_da_1_d = f'\\True Miền nghiệm của bất phương trình (tính cả biên) không chứa gốc tọa độ $O(0;0)$'
            vdc_da_1_s = f'Miền nghiệm của bất phương trình (tính cả biên) có chứa gốc tọa độ $O(0;0)$'
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)
            list_vdc_1 = [vdc_da_1]
            loigiai_vdc_1 = f"Tại $O(0;0)$, ta có $0 \\ge {kt}$ là mệnh đề sai. Vậy miền nghiệm không chứa gốc tọa độ."
            list_vdc_2 = [loigiai_vdc_1]

            # =========================================================================
            # LOGIC XÁO TRỘN VÀ KIỂM TRA ĐIỀU KIỆN 1-3 ĐÁP ÁN ĐÚNG
            # =========================================================================
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

            # Gán lại vào list để xử lý zip
            list_nb_1, list_th_1, list_vd_1, list_vdc_1 = [nb_da_1], [th_da_1], [vd_da_1], [vdc_da_1]

            combined_nb = list(zip(list_nb_1, list_nb_2))
            combined_th = list(zip(list_th_1, list_th_2))
            combined_vd = list(zip(list_vd_1, list_vd_2))
            combined_vdc = list(zip(list_vdc_1, list_vdc_2))

            shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)
            shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)
            shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)
            shuffled_answers_vdc, shuffled_solutions_vdc = zip(*combined_vdc)

            # Xuất nội dung theo định dạng LaTeX
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+
                str(noidungcauhoi)+ 
                '\n\\choiceTFn \n'
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

