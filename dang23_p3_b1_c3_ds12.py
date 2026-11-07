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


def bt_dang23_p3_b1_c3_ds12(self):
                lisdang = ['1']
                dang = random.choice(lisdang)
                
                if dang == '1':
                    # --- Bước 3: Random thông số bài toán ---
                    T = random.choice([10, 12, 15, 20])  # Thời gian tăng tốc (s)
                    # Chọn hệ số góc m sao cho m chia hết cho 2 để v(t) = (m/2)t^2 là số nguyên
                    m_val = random.randint(2, 5) * 2 
                    A_max = m_val * T                    # Gia tốc cực đại tại thời điểm T
                    v0 = random.randint(5, 15)           # Vận tốc ban đầu (m/s)
                    
                    # Tính vận tốc tại thời điểm T: v(T) = (m/2)*T^2 + v0
                    kq_val = (m_val // 2) * (T**2) + v0
                    
                    # Định dạng đáp án đúng
                    da = '$%s$ (m/s)' % latex(kq_val)
                    
                    # --- Bước 4: Tạo phương án sai ---
                    s_wrong = set()
                    while len(s_wrong) < 3:
                        sai_offset = random.choice([-50, -20, 25, 40, 100, -10, 15])
                        sai_val = kq_val + sai_offset
                        if sai_val > 0 and sai_val != kq_val:
                            s_wrong.add('$%s$ (m/s)' % int(sai_val))
                    
                    list_wrong = list(s_wrong)
                    das1, das2, das3 = list_wrong[0], list_wrong[1], list_wrong[2]
                
                    # Tạo mã TikZ cho đồ thị gia tốc
                    # Scale lại tọa độ để hình vẽ cân đối trong LaTeX
                    tikz_code = (r'''\begin{center}
    \begin{tikzpicture}[line join=round, line cap=round, >=stealth, thick, scale=0.05] 
        \draw[->] (0,0) -- (%s,0) node[below] {$t$(s)};
        \draw[->] (0,0) -- (0,%s) node[left] {$a$ (m/s$^2$)};
        \draw[very thick, color=blue] (0,0) -- (%s,%s);
        \draw[dashed] (%s,0) -- (%s,%s) -- (0,%s);
        \node[below] at (%s,0) {$%s$};
        \node[left] at (0,%s) {$%s$};
        \node[below left] at (0,0) {$O$};
    \end{tikzpicture}
    \end{center}''' % (T+10, A_max+15, T, A_max, T, T, A_max, A_max, T, T, A_max, A_max))
                
                    # --- Câu hỏi (Đã sửa lỗi %s% -> %s) ---
                    noidungcauhoi = (r'''Một máy bay đang chuyển động thẳng đều trên mặt đất với vận tốc $v_0 = %s$ (m/s) thì bắt đầu tăng tốc với gia tốc là hàm số $a(t)$ có đồ thị là một đường thẳng đi qua gốc tọa độ như hình vẽ bên dưới.
    %s
    Sau $%s$ giây tăng tốc thì máy bay đạt đến vận tốc đủ lớn để rời khỏi mặt đất. Tính vận tốc của máy bay tại thời điểm bắt đầu rời khỏi mặt đất.''' 
                                     % (v0, tikz_code, T))
                
                    # --- Nội dung lời giải ---
                    loigiai = (r'''Hàm số gia tốc có dạng $a(t) = mt$. Vì đồ thị đi qua điểm $(%s; %s)$ nên: \\
    $%s \cdot m = %s \Rightarrow m = %s$. Vậy $a(t) = %st$ (m/s$^2$). \\
    Vận tốc của máy bay là nguyên hàm của gia tốc: \\
    $v(t) = \int a(t) \text{d}t = \int %st \text{d}t = %st^2 + C$. \\
    Tại thời điểm $t=0$, vận tốc $v(0) = %s \Rightarrow %s \cdot 0^2 + C = %s \Rightarrow C = %s$. \\
    Do đó: $v(t) = %st^2 + %s$. \\
    Vận tốc máy bay tại thời điểm $t = %s$ s là: \\
    $v(%s) = %s \cdot (%s)^2 + %s = %s$ (m/s).'''
                               % (T, A_max, T, A_max, m_val, m_val, 
                                  m_val, m_val // 2, v0, m_val // 2, v0, v0, 
                                  m_val // 2, v0, T, T, m_val // 2, T, v0, kq_val))
                    #Đáp án
                    dapan=' \\shortans[0]{$%s$} '%(latex(kq_val))
    
                    # --- Sắp xếp đáp án ---
                    da_d = '\\True ' + str(da)
                    list_ans = [da_d, str(das1), str(das2), str(das3)]
                    random.shuffle(list_ans)
                
                    # Xuất nội dung theo định dạng LaTeX (ex-choice)
                    content = ('\\begin{minipage}{\\textwidth} \n'
                               '\\begin{ex}\n' + str(noidungcauhoi) +str(dapan)+ '\n'
                               '\\loigiai{' + str(loigiai) + '}\n'
                               '\\end{ex}\n\\end{minipage} \n\n')
                    
                    # Đưa vào QTextEdit
                    return content