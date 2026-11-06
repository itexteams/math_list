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


def bt_dang4_p2_b2_c2_hh10(self):
            # Khai báo biến
            # 1. Random bộ chữ cái đỉnh của hình bình hành và tên giao điểm
            danh_sach_bo_dinh = [
                ['A', 'B', 'C', 'D'],
                ['M', 'N', 'P', 'Q'],
                ['E', 'F', 'G', 'H'],
                ['X', 'Y', 'Z', 'T']
            ]
            bo_dinh = random.choice(danh_sach_bo_dinh)
            giao_diem = random.choice(['O', 'I', 'K', 'H'])

            # 2. Đổi góc nhìn: Chọn ngẫu nhiên 1 đỉnh xuất phát (v0) để áp dụng quy tắc hình bình hành
            idx = random.randint(0, 3)
            v0 = bo_dinh[idx]
            v1 = bo_dinh[(idx + 1) % 4]
            v2 = bo_dinh[(idx + 2) % 4]
            v3 = bo_dinh[(idx + 3) % 4]

            # Tên đa giác theo thứ tự ban đầu để in ra đề bài
            ten_hinh_binh_hanh = f"{bo_dinh[0]}{bo_dinh[1]}{bo_dinh[2]}{bo_dinh[3]}"

            # Nội dung đề bài
            noidungcauhoi = r'Cho hình bình hành $%s$ có $%s$ là giao điểm của hai đường chéo. Khi đó:' % (ten_hinh_binh_hanh, giao_diem)

            ########################################################################
            # Nhận biết ############################################
            # Các đáp án
            nb_da_1_d = r'\True $\overrightarrow{%s%s} + \overrightarrow{%s%s} = \overrightarrow{%s%s}$' % (v0, v1, v0, v3, v0, v2)
            nb_da_1_s = r'$\overrightarrow{%s%s} + \overrightarrow{%s%s} = \overrightarrow{%s%s}$' % (v0, v1, v0, v2, v0, v3)
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_nb_1 = [nb_da_1]

            # Nội dung lời giải tương ứng
            loigiai_nb_d = r'Ta có: $\overrightarrow{%s%s} + \overrightarrow{%s%s} = \overrightarrow{%s%s}$ (quy tắc hình bình hành).' % (v0, v1, v0, v3, v0, v2)
            loigiai_nb_s = r'Ta có: $\overrightarrow{%s%s} + \overrightarrow{%s%s} \neq \overrightarrow{%s%s}$ (theo quy tắc hình bình hành tổng hai cạnh bên bằng đường chéo $\overrightarrow{%s%s}$).' % (v0, v1, v0, v2, v0, v3, v0, v2)
            loigiai_nb_1 = loigiai_nb_d if nb_da_1 == nb_da_1_d else loigiai_nb_s

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
            th_da_1_d = r'\True $\overrightarrow{%s%s} + \overrightarrow{%s%s} = \overrightarrow{%s%s}$' % (v0, v2, v1, v0, v0, v3)
            th_da_1_s = r'$\overrightarrow{%s%s} + \overrightarrow{%s%s} = \overrightarrow{%s%s}$' % (v0, v2, v1, v0, v0, v1)
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_th_1 = [th_da_1]

            # Nội dung lời giải tương ứng
            loigiai_th_d = r'Ta có: $\overrightarrow{%s%s} + \overrightarrow{%s%s} = \overrightarrow{%s%s} + \overrightarrow{%s%s} = \overrightarrow{%s%s} = \overrightarrow{%s%s}$ (vì $%s$ là hình bình hành).' % (v0, v2, v1, v0, v1, v0, v0, v2, v1, v2, v0, v3, ten_hinh_binh_hanh)
            loigiai_th_s = r'Ta có: $\overrightarrow{%s%s} + \overrightarrow{%s%s} = \overrightarrow{%s%s} + \overrightarrow{%s%s} = \overrightarrow{%s%s} \neq \overrightarrow{%s%s}$.' % (v0, v2, v1, v0, v1, v0, v0, v2, v1, v2, v0, v1)
            loigiai_th_1 = loigiai_th_d if th_da_1 == th_da_1_d else loigiai_th_s

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
            vd_da_1_d = r'\True $\left| \overrightarrow{%s%s} + \overrightarrow{%s%s} \right| = %s%s$' % (v0, v1, v0, v3, v0, v2)
            vd_da_1_s = r'$\left| \overrightarrow{%s%s} + \overrightarrow{%s%s} \right| = %s%s$' % (v0, v1, v0, v3, v1, v3)
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vd_1 = [vd_da_1]

            # Nội dung lời giải tương ứng
            loigiai_vd_d = r'Ta có $\left| \overrightarrow{%s%s} + \overrightarrow{%s%s} \right| = \left| \overrightarrow{%s%s} \right| = %s%s$.' % (v0, v1, v0, v3, v0, v2, v0, v2)
            loigiai_vd_s = r'Ta có $\left| \overrightarrow{%s%s} + \overrightarrow{%s%s} \right| = \left| \overrightarrow{%s%s} \right| = %s%s \neq %s%s$.' % (v0, v1, v0, v3, v0, v2, v0, v2, v1, v3)
            loigiai_vd_1 = loigiai_vd_d if vd_da_1 == vd_da_1_d else loigiai_vd_s

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
            vdc_da_1_d = r'\True Nếu $\left| \overrightarrow{%s%s} + \overrightarrow{%s%s} \right| = \left| \overrightarrow{%s%s} - \overrightarrow{%s%s} \right|$ thì $%s$ là hình chữ nhật' % (v0, v1, v0, v3, v2, v1, v2, v3, ten_hinh_binh_hanh)
            vdc_da_1_s = r'Nếu $\left| \overrightarrow{%s%s} + \overrightarrow{%s%s} \right| = \left| \overrightarrow{%s%s} - \overrightarrow{%s%s} \right|$ thì $%s$ là hình thoi' % (v0, v1, v0, v3, v2, v1, v2, v3, ten_hinh_binh_hanh)
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vdc_1 = [vdc_da_1]

            # Nội dung lời giải tương ứng
            loigiai_vdc_1 = r'''Ta có: $\left| \overrightarrow{%s%s} + \overrightarrow{%s%s} \right| = \left| \overrightarrow{%s%s} - \overrightarrow{%s%s} \right| \Leftrightarrow \left| \overrightarrow{%s%s} \right| = \left| \overrightarrow{%s%s} \right| \Leftrightarrow %s%s = %s%s$. \\
            Vì $%s$ là hình bình hành có hai đường chéo bằng nhau nên $%s$ là hình chữ nhật.''' % (v0, v1, v0, v3, v2, v1, v2, v3, v0, v2, v3, v1, v0, v2, v1, v3, ten_hinh_binh_hanh, ten_hinh_binh_hanh)

            # Đưa các lời giải vào danh sách lời giải
            list_vdc_2 = [loigiai_vdc_1]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_vdc = list(zip(list_vdc_1, list_vdc_2))

            # Xáo trộn danh sách kết hợp
            random.shuffle(combined_vdc)

            # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
            shuffled_answers_vdc, shuffled_solutions_vdc = zip(*combined_vdc)


            def count_true_answers(answers):
                return sum(r'\True' in ans for ans in answers)

            # Lập đến khi đáp án có từ 1 đến 3 đúng
            while True:
                nb_da_1 = random.choice(list_nb_da_1)
                th_da_1 = random.choice(list_th_da_1)
                vd_da_1 = random.choice(list_vd_da_1)
                vdc_da_1 = random.choice(list_vdc_da_1)

                answers = [nb_da_1, th_da_1, vd_da_1, vdc_da_1]
                true_count = count_true_answers(answers)

                if 1 <= true_count <= 3:
                    break

            # Cập nhật lại lời giải tương ứng với phương án đã chọn trong vòng lặp
            loigiai_nb_1 = loigiai_nb_d if nb_da_1 == nb_da_1_d else loigiai_nb_s
            loigiai_th_1 = loigiai_th_d if th_da_1 == th_da_1_d else loigiai_th_s
            loigiai_vd_1 = loigiai_vd_d if vd_da_1 == vd_da_1_d else loigiai_vd_s

            # Gán lại vào list
            list_nb_1 = [nb_da_1]
            list_th_1 = [th_da_1]
            list_vd_1 = [vd_da_1]
            list_vdc_1 = [vdc_da_1]

            list_nb_2 = [loigiai_nb_1]
            list_th_2 = [loigiai_th_1]
            list_vd_2 = [vd_da_1] # Giữ đồng bộ gán list cho biến giải của từng cấp độ câu hỏi
            list_vdc_2 = [loigiai_vdc_1]

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

