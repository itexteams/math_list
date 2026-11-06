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


def bt_dang28_p2_b1_c1_ds11(self):
            # Khai báo biến
            # B3-Suy nghĩ tìm cách random bài toán
            # Chọn ngẫu nhiên số đo góc hình học AOM từ danh sách các góc đặc biệt ở góc phần tư thứ I
            goc_list = [30, 45, 60]
            goc_m = random.choice(goc_list)

            # N đối xứng với M qua trục Oy nên góc hình học AON = 180 - goc_m
            goc_n = 180 - goc_m

            # Các góc tính toán cho phương án câu b và câu d
            goc_b_am = goc_m - 360
            goc_d_duong = goc_m - goc_n + 360

            # Vẽ hình bằng TikZ đảm bảo độ dày nét đúng 1pt, màu sắc xanh lam chuyên nghiệp
            tikz_image = ('''\\begin{center} \\begin{tikzpicture}[scale=1.8, line width=1pt, >=stealth]
            \\draw[->, color=blue!70!black] (-1.3,0) -- (1.5,0) node[above] {$x$};
            \\draw[->, color=blue!70!black] (0,-1.3) -- (0,1.5) node[left] {$y$};
            \\draw[color=blue, line width=1pt] (0,0) circle (1);
            \\coordinate (O) at (0,0);
            \\coordinate (A) at (1,0);
            \\coordinate (M) at (%s:1);
            \\draw[line width=1pt] (O) -- (M);
            \\draw[color=blue!70!black] (0.2,0) arc (0:%s:0.2);
            \\node[color=blue!70!black] at (35:0.4) {$%s^\\circ$};
            \\filldraw[fill=blue!20] (O) circle (0pt) node[below left] {$O$};
            \\filldraw[fill=blue!20] (A) circle (0pt) node[below right] {$A$};
            \\filldraw[fill=blue!20] (M) circle (0pt) node[above right] {$M$};
            \\end{tikzpicture} \\end{center}''' %(goc_m, goc_m, goc_m))

            # Nội dung câu hỏi sử dụng định dạng %s theo đúng mẫu yêu cầu
            noidungcauhoi = ('''Trên đường tròn với điểm gốc là $A$. Điểm $M$ thuộc đường tròn sao cho $\\widehat{AOM} = %s^\\circ$ (tham khảo hình vẽ).%s Gọi $N$ là điểm đối xứng với điểm $M$ qua trục $Oy$. Xét tính đúng sai của các khẳng định sau:''' %(goc_m, tikz_image))

            ########################################################################
            # Nhận biết ############################################
            # Khẳng định a (Mẫu gốc: Đúng)
            nb_da_1_d = '\\True sđ$(OA; OM) = %s^\\circ$' %(goc_m)
            nb_da_1_s = 'sđ$(OA; OM) = -%s^\\circ$' %(goc_m)
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)

            list_nb_1 = [nb_da_1]

            loigiai_nb_1 = ('''Do điểm $M$ nằm ở góc phần tư thứ I và quay theo chiều dương nên số đo của góc lượng giác $(OA; OM) = %s^\\circ$.''' %(goc_m))
            list_nb_2 = [loigiai_nb_1]

            combined_nb = list(zip(list_nb_1, list_nb_2))
            random.shuffle(combined_nb)
            shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)

            ########################################################################
            # Thông hiểu ############################################
            # Khẳng định b (Mẫu gốc: Đúng)
            th_da_1_d = '\\True sđ$(OA; OM) = %s^\\circ + k360^\\circ, k \\in \\mathbb{Z}$' %(goc_b_am)
            th_da_1_s = 'sđ$(OA; OM) = %s^\\circ + k180^\\circ, k \\in \\mathbb{Z}$' %(goc_b_am)
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)

            list_th_1 = [th_da_1]

            loigiai_th_1 = ('''Ta có sđ$(OA; OM) = %s^\\circ + k360^\\circ$.\\\\
            Với $k = 1$, ta có $%s^\\circ + 360^\\circ = %s^\\circ$. Do đó khẳng định viết dưới dạng $%s^\\circ + k360^\\circ, k \\in \\mathbb{Z}$ là hoàn toàn chính xác.''' %(goc_b_am, goc_b_am, goc_m, goc_b_am))
            list_th_2 = [loigiai_th_1]

            combined_th = list(zip(list_th_1, list_th_2))
            random.shuffle(combined_th)
            shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)

            ######################################################################## 
            # Vận dụng ############################################
            # Khẳng định c (Mẫu gốc: Đúng)
            vd_da_1_d = '\\True sđ$(OA; ON) = %s^\\circ$' %(goc_n)
            vd_da_1_s = 'sđ$(OA; ON) = %s^\\circ$' %(180 + goc_m)
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)

            list_vd_1 = [vd_da_1]

            loigiai_vd_1 = ('''Vì $N$ đối xứng với $M$ qua trục $Oy$ nên điểm $N$ nằm ở góc phần tư thứ II và có góc hình học $\\widehat{AON} = 180^\\circ - %s^\\circ = %s^\\circ$.\\\\
            Do đó sđ$(OA; ON) = %s^\\circ$.''' %(goc_m, goc_n, goc_n))
            list_vd_2 = [loigiai_vd_1]

            combined_vd = list(zip(list_vd_1, list_vd_2))
            random.shuffle(combined_vd)
            shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)

            ######################################################################## 
            # Vận dụng cao ############################################
            # Khẳng định d (Mẫu gốc: Đúng)
            vdc_da_1_d = '\\True sđ$(ON; OM) = %s^\\circ + k360^\\circ, k \\in \\mathbb{Z}$' %(goc_d_duong)
            vdc_da_1_s = 'sđ$(ON; OM) = -%s^\\circ + k360^\\circ, k \\in \\mathbb{Z}$' %(goc_d_duong)
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)

            list_vdc_1 = [vdc_da_1]

            loigiai_vdc_1 = ('''Ta có sđ$(ON; OM) = \\text{sđ}(OA; OM) - \\text{sđ}(OA; ON) + k360^\\circ = %s^\\circ - %s^\\circ + k360^\\circ = %s^\\circ + k360^\\circ$.\\\\
            Với $k = 1 \\Rightarrow %s^\\circ + 360^\\circ = %s^\\circ$. Do đó khẳng định viết thành $%s^\\circ + k360^\\circ, k \\in \\mathbb{Z}$ là hoàn toàn chính xác.''' 
                             %(goc_m, goc_n, goc_m - goc_n, goc_m - goc_n, goc_d_duong, goc_d_duong))
            list_vdc_2 = [loigiai_vdc_1]

            combined_vdc = list(zip(list_vdc_1, list_vdc_2))
            random.shuffle(combined_vdc)
            shuffled_answers_vdc, shuffled_solutions_vdc = zip(*combined_vdc)

            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            # Lặp đến khi đáp án có từ 1 đến 3 đúng để bảo toàn logic trắc nghiệm Đúng/Sai
            while True:
                nb_da_1 = random.choice(list_nb_da_1)
                th_da_1 = random.choice(list_th_da_1)
                vd_da_1 = random.choice(list_vd_da_1)
                vdc_da_1 = random.choice(list_vdc_da_1)

                answers = [nb_da_1, th_da_1, vd_da_1, vdc_da_1]
                true_count = count_true_answers(answers)

                if 1 <= true_count <= 3:
                    break

            # Gán lại vào list sau khi chọn lọc ngẫu nhiên hợp lệ
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

            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn theo đúng định dạng chuỗi %s
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

