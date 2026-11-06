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


def bt_dang28_p3_b2_c1_ds12(self):
            # Khai báo biến
            def round_SA(a): 
                # Kiểm tra nếu a là số nguyên
                if a == int(a):
                    return "", int(a)

                # Chuyển số thành chuỗi và tách phần nguyên, phần thập phân
                str_a = f"{a:.5f}".rstrip('0')  # Giữ tối đa 5 chữ số thập phân, loại bỏ số 0 dư
                integer_part, _, decimal_part = str_a.partition('.')  # Tách phần nguyên và thập phân

                # Xác định cách làm tròn
                if len(integer_part) > 2:
                    number = Decimal(float(a)).quantize(Decimal('1'), rounding=ROUND_HALF_UP)
                    cirle = "(làm tròn kết quả đến hàng đơn vị)."
                elif len(integer_part) == 2 and len(decimal_part) > 1:
                    number = Decimal(float(a)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
                    cirle = "(làm tròn kết quả đến hàng phần chục)."
                elif len(decimal_part) <= 2:
                    number = str_a  # Không cần làm tròn thêm
                    cirle = ""
                else:
                    number = Decimal(float(a)).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
                    cirle = "(làm tròn kết quả đến hàng phần trăm)."

                # Chuyển dấu chấm thành dấu phẩy (nếu có)
                return cirle, str(number).replace('.', ',')

            # ------------------------------------------------------------------------------BÀI TOÁN
            # 1. Sinh ngẫu nhiên các giá trị gốc cho bài toán
            # Sinh ngẫu nhiên các đối số đầu vào một cách hợp lý
            r = symbols('r')  # Bán kính đáy
            the_tich = 100 * random.randint(5, 15)  # dm³ (thay đổi từ 500 đến 1500 dm³)
            gia_moi_dm2_than, gia_moi_dm2_day = sorted(random.sample(list(range(300, 900)), 2))  
            gia_moi_dm2_than = gia_moi_dm2_than // 50 * 50
            gia_moi_dm2_day = gia_moi_dm2_day // 50 * 50

            # Tính chiều cao dựa trên thể tích
            h = the_tich / (pi * r**2)  
            # Diện tích bề mặt: 2 đáy + thân
            dien_tich_day = 2 * pi * r**2  # Diện tích hai đáy
            dien_tich_than = 2 * the_tich / r  # Diện tích thân
            # Hàm chi phí tổng
            ham_chi_phi = gia_moi_dm2_day * dien_tich_day + gia_moi_dm2_than * dien_tich_than
            # Thay h vào hàm chi phí
            # Đạo hàm để tìm r tối ưu
            diff_ham_chi_phi = diff(ham_chi_phi, r)
            sol = solve(diff_ham_chi_phi, r)
            ban_kinh_toi_uu = sol[0]  
            # Phạm vi bán kính tối ưu
            pham_vi_ban_kinh_toi_uu = random.randint(int(ban_kinh_toi_uu), int(ban_kinh_toi_uu) + 5)

            # Chi phí tối ưu
            chi_phi_toi_uu = ham_chi_phi.subs(r, min(ban_kinh_toi_uu, pham_vi_ban_kinh_toi_uu))
            # Tính kết quả thời gian nhỏ nhất
            ket_qua = chi_phi_toi_uu / 1000

            # 3. Mã TikZ để vẽ hình minh họa
            tikz_code = f"""  \\begin{{tikzpicture}}[scale=.6,line width=1pt,line cap=round,line join=round,font=\\footnotesize]
                \\def\\r{{2}}
                \\def\\h{{5}}
                \\shade[left color=orange!50!yellow, shading angle=90] 
                (-\\r,0) -- (-\\r,\\h) arc (180:0:\\r cm and 0.5cm) -- (\\r,0) arc (0:-180:\\r cm and 0.5 cm) -- cycle ;
                \\draw[thick, orange] (0,\\h) ellipse (\\r cm and 0.5cm);
                \\draw[thick, orange] (-\\r,\\h) -- (-\\r,0) arc (180:360:\\r cm and 0.5cm) -- (\\r,\\h);
                \\draw[dashed, orange, thick] (\\r,0) arc (0:180:\\r cm and 0.5cm);
                \\draw[dashed, thick] (0,0) -- (\\r,0);
                \\filldraw (0,0) circle (1pt);
                \\node at (\\r/2,0.3) {{$ r $}};
                \\node at (\\r + 0.3, \\h/2) {{$ h $}}; 
                \\end{{tikzpicture}} """

            noidungcauhoi = f"""\\immini{{   Người ta cần làm một cái thùng hình trụ có thể tích là ${the_tich}$ dm$^3$. 
                        Giá tiền để sơn hai đáy là ${gia_moi_dm2_day}$ đồng mỗi dm$^2$, và giá tiền để sơn mặt xung quanh là ${gia_moi_dm2_than}$ đồng mỗi dm$^2$. 
                        Biết rằng bán kính $r$ không vượt quá ${pham_vi_ban_kinh_toi_uu}$ dm.
            Chi phí thấp nhất để làm thùng là bao nhiêu nghìn đồng? {round_SA(chi_phi_toi_uu / 1000)[0]}
            }}{{{tikz_code}}}"""
            loigiai = f"""  Gọi bán kính đáy là $r$ (dm) thì chiều cao $h = \\frac{{V}}{{\\pi r^2}} = \\frac{{{the_tich}}}{{\\pi r^2}}$. \\\\
                         Diện tích hai đáy là $S_{{\\text{{đáy}}}} = 2\\pi r^2$, diện tích mặt xung quanh là $S_{{\\text{{xq}}}} = 2\\pi r h = \\frac{{{2 * the_tich}}}{{r}}$. \\\\
                         Chi phí tổng $C(r) = {gia_moi_dm2_day} \\cdot S_{{\\text{{đáy}}}} + {gia_moi_dm2_than} \\cdot S_{{\\text{{xq}}}} = {latex(ham_chi_phi)} $. \\\\
                         Đạo hàm $C'(r) = {latex(diff(ham_chi_phi, r))}$. \\\\
                         Giải $C'(r) = 0$ ta được $r = {latex(nsimplify(ban_kinh_toi_uu))} \\approx {round_SA(ban_kinh_toi_uu)[1]} $. \\\\
                         Vì $r \\approx {round_SA(ban_kinh_toi_uu)[1]}$ {'không' if ban_kinh_toi_uu > pham_vi_ban_kinh_toi_uu else ''} thoả điều kiện $0 < r \\le {pham_vi_ban_kinh_toi_uu}$ nên bán kính để chi phí thấp nhất là $r = {latex(min(ban_kinh_toi_uu, pham_vi_ban_kinh_toi_uu))}$ dm. \\\\
                         Chi phí chi phí thấp nhất là ${latex(nsimplify(chi_phi_toi_uu))}$ đồng $\\approx {round_SA(chi_phi_toi_uu)[1]}$ đồng $\\approx {round_SA(ket_qua)[1]}$ nghìn đồng. """
            #Đáp án
            dapan='\\shortans[0]{$%s$}'%(round_SA(ket_qua)[1])              

            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+str(dapan)+
                '\\loigiai{ \n'
                +str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n').replace('$zz$','.').replace('\\frac','\\dfrac')
            return content         

