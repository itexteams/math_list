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


def bt_dang34_p3_b6_c2_hh11(self):
                # Khai báo biến
                # B3: Random thông số bài toán
                side = random.randint(2, 10) # Cạnh đáy
                
                # Tính toán logic
                # Diện tích đáy ABC (tam giác đều): S = (side^2 * sqrt(3)) / 4
                s_abc_val = (side**2 * math.sqrt(3)) / 4
                # AM là đường cao tam giác đều: AM = (side * sqrt(3)) / 2
                am_val = (side * math.sqrt(3)) / 2
                # SA = AM (do tam giác SAM vuông cân tại A)
                sa_val = am_val
                # Thể tích V = 1/3 * SA * S_ABC
                v_val = (1/3) * sa_val * s_abc_val
                
                # Định dạng số (thay dấu chấm bằng dấu phẩy cho chuẩn VN)
                def format_vn(num):
                    return f"{round(num, 1)}".replace('.', ',')

                da_dung_val = round(v_val, 1)
                da_dung_str = format_vn(da_dung_val)
                
                # B4: Tạo các phương án sai (không trùng đáp án đúng)
                s_sai = set()
                while len(s_sai) < 3:
                    # Tạo các biến thể sai dựa trên các lỗi hay gặp
                    sai_1 = round(v_val * random.uniform(0.5, 1.5), 1)
                    sai_2 = round((side**3 * math.sqrt(3)) / 12, 1) # Thiếu 1/3 hoặc nhầm SA
                    sai_3 = round((side**3) / 4, 1)
                    
                    candidates = [sai_1, sai_2, sai_3, round(da_dung_val + random.randint(1, 5), 1)]
                    for c in candidates:
                        if c != da_dung_val and len(s_sai) < 3:
                            s_sai.add(format_vn(c))

                list_sai = list(s_sai)
                
                # Trộn đáp án
                da_d = '\\True $' + da_dung_str + '$'
                list_1 = [da_d, '$' + list_sai[0] + '$', '$' + list_sai[1] + '$', '$' + list_sai[2] + '$']
                random.shuffle(list_1)

                # Nội dung hình vẽ TikZ
                tikz_code = r"""\begin{center}
    \begin{tikzpicture}[line cap=round,line join=round, line width=1pt, scale=0.8]
        \coordinate (A) at (0,0);
        \coordinate (B) at (-1.5,-1.5);
        \coordinate (C) at (3,-1);
        \coordinate (S) at (0,3.5);
        \coordinate (M) at ($(B)!0.5!(C)$);
        \coordinate (H) at ($(S)!0.6!(M)$);
        \draw [dash pattern=on 3pt off 3pt] (S)--(A) (A)--(B) (A)--(C) (A)--(M) (A)--(H);
        \draw (S)--(B)--(C)--(S) (S)--(M);
        \draw (0,0.3)--(-0.3,0.3)--(-0.3,0); 
        \draw (S) node[above] {$S$};
        \draw (A) node[left] {$A$};
        \draw (B) node[below left] {$B$};
        \draw (C) node[right] {$C$};
        \draw (M) node[below right] {$M$};
        \draw (H) node[above right] {$H$};
        \fill (S) circle (1.2pt) (A) circle (1.2pt);
    \end{tikzpicture}
    \end{center}"""

                # B2: Viết lại nội dung câu hỏi
                noidungcauhoi = (f"Cho hình chóp $S.ABC$ có đáy $ABC$ là tam giác đều cạnh bằng ${side}$, cạnh bên $SA$ vuông góc với mặt phẳng đáy, "
                                f"góc giữa $SA$ và mặt phẳng $(SBC)$ bằng $45^\\circ$. "
                                f"Thể tích khối chóp $S.ABC$ bằng bao nhiêu (làm tròn kết quả đến hàng phần chục)?")

                # Nội dung lời giải
                loigiai = (f"{tikz_code}\n"
                        f"Gọi $M$ là trung điểm $BC$ thì $AM \\perp BC$ và $SA \\perp BC$ nên $BC \\perp (SAM)$.\n"
                        f"Kẻ $AH \\perp SM$ tại $H$ thì $AH \\perp (SBC)$. Suy ra góc giữa $SA$ và mặt phẳng $(SBC)$ bằng "
                        f"$\\widehat{{ASH}} = \\widehat{{ASM}} = 45^\\circ$. Do đó, $\\Delta SAM$ vuông cân ở $A$ và $SA = AM = \\frac{{{side} \\sqrt{{3}}}}{{2}} \\approx {format_vn(am_val)}$.\\\\\n"
                        f"Diện tích tam giác đều $ABC$ là $S_{{ABC}} = \\frac{{{side}^2 \\sqrt{{3}}}}{{4}} \\approx {format_vn(s_abc_val)}$.\\\\\n"
                        f"Suy ra $V_{{S.ABC}} = \\frac{{1}}{{3}} \\cdot SA \\cdot S_{{ABC}} \\approx \\frac{{1}}{{3}} \\cdot {format_vn(sa_val)} \\cdot {format_vn(s_abc_val)} \\approx {da_dung_str}$.")
                dapan = '\\shortans[0]{$%s$}\n' % (da_dung_str)
                # B1 & B2: Xuất câu trắc nghiệm đúng mẫu
                content = (
                    '\\begin{minipage}{\\textwidth} \n'
                    '\\begin{ex}\n' + noidungcauhoi + str(dapan)+
                    '\\loigiai{' + loigiai + '}\n'
                    '\\end{ex}\n'
                    '\\end{minipage} \n\n' )
                return content